def parse_words(raw_words: str) -> list[str]:
    """Remove brackets and commas from string."""
    return raw_words.replace(" ", "").replace("[", "").replace("]", "").split(",")


def main():
    words = parse_words(input("Enter words to count: "))
    unique_words = set()

    for word in words:
        unique_words.add(word)

    print(sorted(list(unique_words)))


if __name__ == "__main__":
    main()
