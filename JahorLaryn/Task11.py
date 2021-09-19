from functools import reduce


def combine_dicts(*args):
    """A function, that receives changeable number of dictionaries
    (keys - letters, values - numbers) and combines them into one dictionary.
    Dict values ​​should be summarized in case of identical keys."""
    keys = reduce((lambda x, y: set(x) | set(y)), args)
    return {k: reduce((lambda x, y: x.get(k, 0) + y.get(k, 0)), args) for k in keys}
