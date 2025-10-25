import aio_pika
import json

async def send_task(task, queue_name="api_tasks"):
	connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")

	async with connection:
		channel = await connection.channel()
		await channel.declare_queue(queue_name, durable=True)

		message = aio_pika.Message(body=json.dumps(task).encode(), delivery_mode=aio_pika.DeliveryMode.PERSISTENT)

		await channel.default_exchange.publish(message, routing_key=queue_name)
		print(f"Задача отправлена в очередь: {task['name']}")