def main():
    dicts = eval(input("Enter pairs with a number and value: "))
    unique_items = set()
    for dict in dicts:
        for item in dict.values():
            unique_items.add(item)
    print(unique_items)


if __name__ == "__main__":
    main()
