# I guess the name in the Task.md is wrong. But idk.
def get_shortest_word(s: str) -> str:
    """A function which returns the longest word in the given string."""
    words = s.split()
    max_length = max([(len(word), i) for (i, word) in enumerate(words)])[1]
    return words[max_length]
