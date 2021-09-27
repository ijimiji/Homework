def most_common_words(filepath, number_of_words=3):
    """A function which search for most common words in the file."""
    freqs = {}
    with open(filepath, "r") as f:
        items = [
            item.lower() for item in f.read().replace(",", "").replace(".", "").split()
        ]
        for item in items:
            if item in freqs:
                freqs[item] += 1
            else:
                freqs[item] = 0
    sorted_items = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
    return [word for (word, freq) in sorted_items[:number_of_words]]


def main():
    print(most_common_words("data/lorem_ipsum.txt"))


if __name__ == "__main__":
    main()
