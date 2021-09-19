import string


def split(s: str, separator=None, maxsplit=-1) -> list[str]:
    """A function which works the same as `str.split` method."""
    # By default .split uses whitespace as a separator
    if separator:
        separator = [separator]
    else:
        separator = string.whitespace
    substring_beginning = 0
    substrings = []
    n = len(s)
    for i in range(n):
        if maxsplit != 0:
            if s[i] in separator or i == n - 1:
                substrings.append(s[substring_beginning : i + 1])
                maxsplit -= 1
                substring_beginning = i
        else:
            substrings.append(s[substring_beginning:n])
    return substrings
