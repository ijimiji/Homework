def is_palidrome(s: str) -> bool:
    """A function that checks whether a string is a palindrome or not."""
    n: int = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True
