"""Write a Python program to sort a dictionary by key."""


def keys_values_to_dict(keys_values: list[str]) -> dict:
    """Return dict made with grouped keys-values from a given list."""
    dict = {}
    for i in range(0, len(keys_values), 2):
        dict[keys_values[i]] = keys_values[i + 1]
    return dict


def main():
    key_values = (
        input("Enter keys and values separated by commas: ").replace(" ", "").split(",")
    )
    dict = keys_values_to_dict(key_values)
    sorted_dict = {}
    for key in sorted(dict.keys()):
        sorted_dict[key] = dict[key]
    dict = sorted_dict
    print(dict)


if __name__ == "__main__":
    main()
