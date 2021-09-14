def main():
    string = input("Enter string to count the number of characters: ")
    char_frequences = {}
    for char in string:
        downcased_char = char.lower()
        if downcased_char in char_frequences:
            char_frequences[downcased_char] += 1
        else:
            char_frequences[downcased_char] = 1

    print(char_frequences)


if __name__ == "__main__":
    main()
