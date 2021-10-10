#!/usr/bin/env python3
from cli import parse_args, handle_args, RSSReader, RSSExporter


def main():
    args = parse_args()
    settings = handle_args(args)
    rss = RSSReader(settings["source"], settings)
    rss_exporter = RSSExporter(rss)
    print(rss)
    for format in settings["export_queue"]:
        rss_exporter.export(format)


if __name__ == "__main__":
    main()
