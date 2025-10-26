from kafka import KafkaConsumer
import json

from .logger import setup_logger
from .storage import save_results

log = setup_logger()

consumer = KafkaConsumer('api_results', bootstrap_servers='localhost:9092',
												 auto_offset_reset='earliest', group_id='api_monitor_group',
												 value_deserializer=lambda m: json.loads(m.decode('utf-8')))
results_batch = []

for message in consumer:
	result = message.value
	log.info(f"[CONSUMER] The result is obtained: {result['name']} -> {result['status']}")
	results_batch.append(result)

save_results(results_batch)
log.info(f"[CONSUMER] Saving the results")
results_batch.clear()