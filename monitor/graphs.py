from pathlib import Path
import json
import matplotlib.pyplot as plt
from collections import defaultdict
from statistics import mean

def timeDispersion(log):
	json_path = Path("logs/api_log.json")
	if not json_path.exists():
		log.error("There is no data for analysis! You need to run the \"check\" command")
		return

	with json_path.open("r", encoding="utf-8") as f:
		data = json.load(f)

	success = [d for d in data if d["status"] == 200]

	# x - Имя эндпоинта, y - Время отклика эндпоинта
	x = [d["name"] for d in success]
	y = [d["response_time_ms"] for d in success]

	plt.figure(figsize=(10, 5))
	plt.scatter(x, y, c=y, alpha=0.6)
	plt.colorbar(label="Response Time (ms)")
	plt.title("Response time dispersion for successful requests")
	plt.xlabel("Endpoint")
	plt.ylabel("Response Time (ms)")
	plt.xticks(rotation=45, ha="right")
	plt.grid(alpha=0.3)
	plt.tight_layout()
	plt.gcf().canvas.manager.set_window_title("Dispersion")
	plt.show()

def timeAverage(log):
	json_path = Path("logs/api_log.json")
	if not json_path.exists():
		log.error("There is no data for analysis! You need to run the \"check\" command")
		return

	with json_path.open("r", encoding="utf-8") as f:
		data = json.load(f)

	success = [d for d in data if d["status"] == 200]

	endpoint_times = defaultdict(list)
	for d in success:
		endpoint_times[d["name"]].append(d["response_time_ms"])

	# x - Имя эндпоинта, y - Среднее время отклика эндпоинта
	x = list(endpoint_times.keys())
	y = [mean(times) for times in endpoint_times.values()]

	plt.figure(figsize=(10, 5))
	plt.bar(x, y, color="skyblue")
	plt.title("Response time dispersion for successful requests")
	plt.xlabel("Endpoint")
	plt.ylabel("Response Time (ms)")
	plt.xticks(rotation=45)
	plt.grid(alpha=0.3)
	plt.tight_layout()
	plt.gcf().canvas.manager.set_window_title("Average")
	plt.show()