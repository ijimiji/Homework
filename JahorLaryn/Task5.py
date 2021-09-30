class NotEvenError(ValueError):
    pass


class LessThanTwoError(ValueError):
    pass


def EvenGt2(x):
    if x % 2:
        raise NotEvenError("Value is not even")
    if x < 2:
        raise LessThanTwoError("Value is less than 2")
    return True
