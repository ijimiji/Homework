def get_pairs(lst: list):
    """A function which returns a list of tuples containing pairs of elements.
    If there is only one element in the list returns None instead."""
    if len(lst) < 2:
        return None
    return [(lst[i], lst[i + 1]) for i in range(len(lst) - 1)]
