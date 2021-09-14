def main():
    string = input("Enter string to count it's contents: ")
    print(string.rindex(string[-1]) + 1)


if __name__ == "__main__":
    main()
