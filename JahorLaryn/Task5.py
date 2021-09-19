def get_digits(number: int) -> tuple[int, ...]:
    """A function which returns a tuple of a given integer's digits."""
    return tuple(int(digit) for digit in str(number))
