from string import ascii_lowercase
from functools import reduce

# Implement a bunch of functions which receive a changeable number of strings and return next parameters:


def test_1_1(*strings):
    """Returns characters that appear in all strings"""
    all_in = lambda x, xs: reduce((lambda x, y: x and y), [x in s for s in strings])
    return [char for char in ascii_lowercase if all_in(char, strings)]


def test_1_2(*strings):
    """Returns characters that appear in at least one string"""
    at_least_one_in = lambda x, xs: reduce(
        (lambda x, y: x or y), [x in s for s in strings]
    )
    return [char for char in ascii_lowercase if at_least_one_in(char, strings)]


def test_1_3(*strings):
    """Returns characters that appear at least in two strings"""
    two_in = lambda x, xs: [x in s for s in strings].count(True) >= 2
    return [char for char in ascii_lowercase if two_in(char, strings)]


def test_1_4(*strings):
    """Returns characters of alphabet, that were not used in any string."""
    return [char for char in ascii_lowercase if not char in strings]
