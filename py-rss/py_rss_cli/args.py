import argparse
import sys
from py_rss_cli.version import print_version_and_exit, version


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="RSS URL", nargs="?")
    parser.add_argument("--version", action="store_true", help="Print version info")
    parser.add_argument(
        "--json", action="store_true", help="Print result as JSON in stdout"
    )
    parser.add_argument(
        "--verbose", action="store_true", help="Outputs verbose status messages"
    )
    parser.add_argument("--limit", help="Limit news topics if this parameter provided")
    return parser.parse_args()


def handle_args(args):
    return {
        "version": print_version_and_exit() if args.version else version,
        "limit": int(args.limit) if args.limit else None,
        "json": True if args.json else False,
        "verbose": True if args.verbose else False,
        "source": args.source
        if args.source
        else (print("error: RSS URL is required"), sys.exit()),
    }
