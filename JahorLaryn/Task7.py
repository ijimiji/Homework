from functools import reduce


def foo(numbers: list[int]) -> list[int]:
    """A function which, given a list of integers,
    returns a new list such that each element at index i of the new list is the product
    of all the numbers in the original array except the one at i."""
    multiply = lambda lst: reduce((lambda x, y: x * y), lst)
    remove = lambda xs, filter_element: [x for x in xs if x != filter_element]
    return [multiply(remove(numbers, number)) for number in numbers]
