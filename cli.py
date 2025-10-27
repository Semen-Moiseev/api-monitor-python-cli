import argparse
import asyncio
from monitor import monitor, logger, stats, graphs

def main():
	parser = argparse.ArgumentParser(description="API Monitor CLI")
	subparsers = parser.add_subparsers(dest="command", help="Commands")

	# Команда check
	parser_check = subparsers.add_parser("check", help="Check the API from the configuration")
	parser_check.add_argument("config", help="Endpoints file path")

	# Команда stats
	parser_stats = subparsers.add_parser("stats", help="Show brief statistics")

	# Команда graphs
	parser_graphs = subparsers.add_parser("graphs", help="Show graphs")
	parser_graphs.add_argument("--dispersion", action="store_true", help="Conclusion of the graph of the temporal dispersion of successful requests")
	parser_graphs.add_argument("--average", action="store_true", help="Conclusion on the average endpoint time schedule")

	args = parser.parse_args()
	log = logger.setup_logger()

	if args.command == "check":
		asyncio.run(monitor.run_check_async(args.config, log))
	elif args.command == "stats":
		stats.show_stats(log)
	elif args.command == "graphs":
		if args.dispersion:
			graphs.timeDispersion(log)
		elif args.average:
			graphs.timeAverage(log)
	else:
		while True:
			cmd = input("Enter command (check, stats, graphs, exit): ").strip()
			if cmd == "exit":
				break
			elif cmd == "check":
				config = input("Enter path to the configuration file: ").strip()
				asyncio.run(monitor.run_check_async(config, log))
			elif cmd == "stats":
				stats.show_stats(log)
			elif cmd == "graphs --dispersion":
				graphs.timeDispersion(log)
			elif cmd == "graphs --average":
				graphs.timeAverage(log)
			else:
				print("Unknown command!")

if __name__ == "__main__":
	main()