def substitute_quotes(string_with_quotes: str) -> str:
    """A function which receives a string and replaces all `"` symbols
    with `'` and vise versa."""
    s = list(string_with_quotes)
    for i in range(len(s)):
        if s[i] == "'":
            s[i] == '"'
        if s[i] == '"':
            s[i] == "'"
    return "".join(s)
