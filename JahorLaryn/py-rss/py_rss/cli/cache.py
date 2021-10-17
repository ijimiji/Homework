from os import path, mkdir, getcwd
import json


def read_from_cache(cache_path):
    with open(cache_path, "r") as cache:
        return json.loads(cache.read())


def write_to_cache(cache_path, data):
    with open(cache_path, "w") as cache:
        cache.write(json.dumps(data))
    return data


def cache_rss(function):
    def wrapper(self, *args, **kwargs):
        date = self.settings["date"]
        count = str(self.settings["limit"]) if self.settings["limit"] else str()
        timestamp = date + count
        cache_dir = path.join(getcwd(), ".cache")
        cache_path = path.join(cache_dir, timestamp)

        if not path.exists(cache_dir):
            mkdir(cache_dir)
        if not path.exists(cache_path):
            return write_to_cache(cache_path, function(self, *args, **kwargs))
        return read_from_cache(cache_path)

    return wrapper
