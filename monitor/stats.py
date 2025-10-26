from pathlib import Path
import json
import pandas as pd

def show_stats(log):
	json_path = Path("logs/api_log.json")

	if not json_path.exists():
		log.error("There is no data for analysis! You need to run the \"check\" command")
		return

	with json_path.open("r", encoding="utf-8") as f:
		data = json.load(f)

	total_requests = len(data)
	if total_requests == 0:
		log.error("There is no data for analysis! You need to run the \"check\" command")

	success = [d for d in data if d["status"] == 200]
	response_times = [r["response_time_ms"] for r in success]
	avg_time = sum(response_times) / total_requests
	min_time = min(response_times)
	max_time = max(response_times)

	log.info(f"Checks: {total_requests}")
	log.info(f"Success: {len(success)} ({len(success) / total_requests * 100:.1f}%)")
	log.info(f"Average response time: {avg_time:.2f} ms")
	log.info(f"Min response time: {min_time} ms")
	log.info(f"Max response time: {max_time} ms")