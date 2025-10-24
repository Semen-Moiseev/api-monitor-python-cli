import argparse
from monitor import monitor, logger, stats

def main():
	parser = argparse.ArgumentParser(description="API Monitor CLI")
	subparsers = parser.add_subparsers(dest="command", help="Commands")

	# Команда check
	parser_check = subparsers.add_parser("check", help="Check the API from the configuration")
	parser_check.add_argument("config", help="Endpoints file path")

	# Команда stats
	parser_stats = subparsers.add_parser("stats", help="Show brief statistics")

	args = parser.parse_args()
	log = logger.setup_logger()

	if args.command == "check":
		monitor.run_monitor(args.config, log)
	elif args.command == "stats":
		stats.show_stats(log)
	else:
		parser.print_help()

if __name__ == "__main__":
	main()