def call_once(function):
    cache = {}

    def wrapper(*args):
        if not "cached result" in cache:
            cache["cached result"] = function(*args)
        return cache["cached result"]

    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


def main():
    print(sum_of_numbers(1336, 1))
    print(sum_of_numbers(16, 1))


if __name__ == "__main__":
    main()
