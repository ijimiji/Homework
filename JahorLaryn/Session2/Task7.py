def main():
    number = 0
    numbers = eval(input("Enter a tupple of numbers: "))
    for (degree, digit) in enumerate(numbers[::-1]):
        number += digit * (10 ** degree)
    print(number)


if __name__ == "__main__":
    main()
