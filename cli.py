import argparse
import asyncio
from monitor.monitor import run_check_async
from monitor.stats import show_stats

def main():
	parser = argparse.ArgumentParser(description="API Monitor CLI")
	subparsers = parser.add_subparsers(dest="command", help="Commands")

	# Команда check
	parser_check = subparsers.add_parser("check", help="Check the API from the configuration")
	parser_check.add_argument("config", help="Endpoints file path")

	# Команда stats
	parser_stats = subparsers.add_parser("stats", help="Show brief statistics")

	args = parser.parse_args()

	if args.command == "check":
		asyncio.run(run_check_async(args.config))
	elif args.command == "stats":
		show_stats()
	else:
		parser.print_help()

if __name__ == "__main__":
	main()