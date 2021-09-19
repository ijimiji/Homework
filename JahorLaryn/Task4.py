def split_by_index(s: str, indexes: list[int]) -> list[str]:
    """A function which splits the s string by indexes specified in indexes.
    Wrong indexes are ignored"""
    substring_beginning = 0
    substrings = []
    n = len(s)
    for i in range(n):
        if i in indexes or i == n - 1:
            substrings.append(s[substring_beginning : i + 1])
            substring_beginning = i
    if not substrings:
        return [s]
    return substrings
