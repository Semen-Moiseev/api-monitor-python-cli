import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def setup_logger():
	Path("logs").mkdir(exist_ok=True)

	log = logging.getLogger("api_monitor")
	log.setLevel(logging.INFO)

	formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

	file_handler = RotatingFileHandler("logs/api_monitor.log", maxBytes=1_000_000, backupCount=3, encoding="utf-8") # max 1MB
	file_handler.setFormatter(formatter)
	if not log.handlers:
		log.addHandler(file_handler)

	console_handler = logging.StreamHandler()
	console_handler.setFormatter(formatter)
	log.addHandler(console_handler)

	return log