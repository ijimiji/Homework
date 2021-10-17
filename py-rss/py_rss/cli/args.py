import argparse
from cli.version import print_version_and_exit, version
from datetime import datetime


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="RSS URL", nargs="?")
    parser.add_argument(
        "--daemon",
        help="Run py-rss as a daemon to serve the server",
        action="store_true",
    )
    parser.add_argument(
        "--date",
        help="Try to fetch RSS from given date and use cached result if possible",
    )
    parser.add_argument("--version", action="store_true", help="Print version info")
    parser.add_argument(
        "--json", action="store_true", help="Print result as JSON in stdout"
    )
    parser.add_argument(
        "--verbose", action="store_true", help="Outputs verbose status messages"
    )
    parser.add_argument("--to_epub", action="store_true", help="Converts news to epub")
    parser.add_argument("--to_html", action="store_true", help="Converts news to html")
    parser.add_argument("--limit", help="Limit news topics if this parameter provided")
    return parser.parse_args()


def handle_args(args):
    time = datetime.now().strftime("%Y%d%m")
    return {
        "version": print_version_and_exit() if args.version else version,
        "limit": int(args.limit) if args.limit else None,
        "json": True if args.json else False,
        "date": args.date if args.date else time,
        "daemon": True if args.daemon else False,
        "verbose": True if args.verbose else False,
        "export_queue": [
            "epub" if args.to_epub else None,
            "html" if args.to_html else None,
        ],
        "source": args.source if args.source else None,
    }
