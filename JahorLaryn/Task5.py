def remember_result(function):
    """A decorator `remember_result`
    which remembers last result of function it decorates and prints
    it before next call."""
    cache = {"last": None}

    def wrapper(*args):
        print(f"Last result = {cache['last']}")
        cache["last"] = function(*args)

    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result


def main():
    sum_list("a", "b")
    sum_list("a", "c")


if __name__ == "__main__":
    main()

# Wanted to mention a shorter version which is not considered to be
# a solution by me as it accepts extra dummy arg
# def remember_result(func):
#     """A decorator `remember_result`
#     which remembers last result of function it decorates and prints
#     it before next call."""
#     def wrapper(*args, last_result=[None]):
#         print(f"Last result = {last_result[0]}")
#         last_result[0] = func(*args)
#     return wrapper