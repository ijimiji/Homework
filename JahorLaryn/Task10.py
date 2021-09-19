def generate_squares(n: int):
    """Generates n first squares with a dict."""
    return {n: n * n for n in range(1, n + 1)}
