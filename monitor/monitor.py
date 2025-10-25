# from monitor.storage import save_results
from .rabbitmq_producer import send_task

from pathlib import Path
from datetime import datetime
import json
import requests
import time
import asyncio
import aiohttp

# Асинхронная проверка одного API
async def fetch(session, name, url, log, semaphore):
	async with semaphore:
		start_resp_time = time.time()

		try:
			async with session.get(url, timeout=aiohttp.ClientTimeout(total=3)) as response:
				response.raise_for_status()
				await response.text()
				status = response.status
				elapsed_resp_time = int((time.time() - start_resp_time) * 1000)

				log.info(f"Check {name} -> {status} ({elapsed_resp_time} ms)")
		except (aiohttp.ClientError, asyncio.TimeoutError):
			status = response.status
			elapsed_resp_time = int((time.time() - start_resp_time) * 1000)

			log.error(f"Check {name} -> {status}: Request error ({elapsed_resp_time} ms)")

	return {
		"name": name,
		"url": url,
		"status": status,
		"response_time_ms": elapsed_resp_time,
		"timestamp": datetime.now().isoformat()
	}

# Асинхронная проверка всех API из файла конфигурации
async def run_check_async(config_path, log):
	path = Path(config_path)
	if not path.exists():
		log.error(f"File {config_path} not found!")
		return

	with path.open("r", encoding="utf-8") as f:
		endpoints = json.load(f)

	for endpoint in endpoints:
		await send_task(endpoint)

		# async with aiohttp.ClientSession() as session:
		# 	tasks = [fetch(session, endpoint, log, semaphore) for endpoint in endpoints]
		# 	results = await asyncio.gather(*tasks, return_exceptions=True)

		# save_results(results)
		# log.info("The results are saved.")