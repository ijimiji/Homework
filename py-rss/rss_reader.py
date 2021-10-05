#!/usr/bin/env python3
from py_rss_cli import parse_args, handle_args, ReadRSS


def main():
    args = parse_args()
    settings = handle_args(args)
    print(ReadRSS(settings["source"], settings))


if __name__ == "__main__":
    main()
