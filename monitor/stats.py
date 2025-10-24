from pathlib import Path
import json

def show_stats(log):
	json_path = Path("logs/api_log.json")

	if not json_path.exists():
		log.error("There is no data for analysis! You need to run the \"check\" command")
		return

	with json_path.open("r", encoding="utf-8") as f:
		data = json.load(f)
		total = len(data)

	if total == 0:
		log.error("There is no data for analysis! You need to run the \"check\" command")

	success = [d for d in data if d["status"] == 200]
	avg_time = round(sum(d["response_time_ms"] for d in data) / total, 2)

	log.info(f"Checks: {total}")
	log.info(f"Success: {len(success)} ({round(len(success) / total * 100, 1)}%)")
	log.info(f"Average response time: {avg_time} ms")