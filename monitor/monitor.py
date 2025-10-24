from monitor.storage import save_results

from pathlib import Path
from datetime import datetime
import json
import requests
import time

def run_monitor(config_path, log):
	path = Path(config_path)
	if not path.exists():
		log.error(f"File {config_path} not found!")
		return

	with path.open("r", encoding="utf-8") as f:
		endpoints = json.load(f)

	results = []

	for endpoint in endpoints:
		name = endpoint.get("name")
		url = endpoint.get("url")

		start_resp_time = time.time()
		try:
			response = requests.get(url, timeout=5)
			status = response.status_code
		except requests.exceptions.RequestException:
			log.error(f"{name}: Request error")
			status = None

		elapsed_resp_time = int((time.time() - start_resp_time) * 1000)

		result = {
			"name": name,
			"url": url,
			"status": status,
			"response_time_ms": elapsed_resp_time,
			"timestamp": datetime.now().isoformat()
		}
		log.info(f"Check {name} -> {status} ({elapsed_resp_time} ms)")
		results.append(result)

	save_results(results)
	log.info("The results are saved.")