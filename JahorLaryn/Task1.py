from os import remove


def sort_names(file_input: str, file_output: str):
    with open(file_input, "r") as unsorted_names:
        with open(file_output, "w") as sorted_names:
            sorted_names.write("\n".join(sorted(unsorted_names.read().split())))


def main():
    sort_names("data/unsorted_names.txt", "data/sorted_names.txt")


if __name__ == "__main__":
    main()
