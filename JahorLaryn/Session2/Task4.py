def get_divisors(number: int) -> set[int]:
    """Return a set of divisors of a number."""
    divisors = set()
    for divisor in range(1, number + 1):
        if number % divisor == 0:
            divisors.add(divisor)
    return divisors


def main():
    number = int(input("Enter a number to get divisors: "))
    print(get_divisors(number))


if __name__ == "__main__":
    main()
