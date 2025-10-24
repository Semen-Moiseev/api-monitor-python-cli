from pathlib import Path
import json
import csv

def save_results(results):
	Path("logs").mkdir(exist_ok=True)
	json_path = Path("logs/api_log.json")
	csv_path = Path("logs/api_log.csv")

	if json_path.exists():
		with json_path.open("r", encoding="utf-8") as f:
			old_data = json.load(f)
	else:
		old_data = []

	old_data.extend(results)

	with json_path.open("w", encoding="utf-8") as f:
		json.dump(old_data, f, indent=2, ensure_ascii=False)

	with csv_path.open("a", newline="", encoding="utf-8") as f:
		writer = csv.DictWriter(f, fieldnames=results[0].keys())
		if f.tell() == 0:
			writer.writeheader()
		writer.writerows(results)