#!/usr/bin/env python3
from cli import parse_args, handle_args, RSSReader, RSSExporter
from api import app
import sys


def export_rss(rss, export_queue):
    rss_exporter = RSSExporter(rss)
    for format in export_queue:
        rss_exporter.export(format)


def main():
    args = parse_args()
    settings = handle_args(args)
    if settings["daemon"]:
        print("Daemon")
        app.run(port=3000)
    else:
        if not settings["source"]:
            print("URL is required!")
            sys.exit()
        rss = RSSReader(settings["source"], settings)
        # Print the RSS feed
        print(rss)
        # Export RSS if any formats are provided
        export_rss(rss.as_dicts(), settings["export_queue"])


if __name__ == "__main__":
    main()
