import aio_pika
import json
import aiohttp
import asyncio

from .monitor import fetch
from .logger import setup_logger
from .storage import save_results

# Число одновременных запросов
SEMAPHORE_LIMIT = 5
MAX_BATCH_SIZE = 11

async def worker(queue_name="api_tasks"):
	log = setup_logger()
	connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")

	async with connection:
		channel = await connection.channel()
		queue = await channel.declare_queue(queue_name, durable=True)
		print(f"[WORKER] Слушаем очередь {queue_name}")

		while True:
			endpoints = []

			async with queue.iterator() as queue_iter:
				async for message in queue_iter:
					async with message.process():
						endpoint = json.loads(message.body)
						endpoints.append(endpoint)

					if len(endpoints) >= MAX_BATCH_SIZE:
						break

			if endpoints:
				async with aiohttp.ClientSession() as session:
					tasks = [fetch(session, endpoint['name'], endpoint['url'], log, asyncio.Semaphore(SEMAPHORE_LIMIT)) for endpoint in endpoints]
					results = await asyncio.gather(*tasks, return_exceptions=True)
					endpoints = []

				save_results(results)
				log.info("The results are saved.")
			else:
				await asyncio.sleep(1)


if __name__ == "__main__":
	print(f"[WORKER] Запуск RabbitMQ...")
	asyncio.run(worker())