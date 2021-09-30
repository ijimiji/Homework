from Task5 import EvenGt2, LessThanTwoError, NotEvenError


def eratosthenes(n):
    primes = list(range(2, n + 1))
    for i in primes:
        j = 2
        while i * j <= primes[-1]:
            if i * j in primes:
                primes.remove(i * j)
            j = j + 1
    return primes


def odd_primes(N):
    oddprimes = eratosthenes(N)
    # oddprimes.remove(2)
    return oddprimes


def checkGoldbachConjecture(n):
    x, y = 0, 0
    result = 0
    prime = odd_primes(n)
    while result != n:
        for i in range(len(prime)):
            if result == n:
                break  # this line first
            x = prime[i]  # this line after
            for j in range(len(prime)):
                y = prime[j]
                result = x + y
                if result == n:
                    break
    return x, y


while True:
    print("Enter q to exit this program.")
    choice = input("Or enter a number to check Goldbach conjecture: ")
    if choice == "q":
        print("Bye!")
        break
    n = int(choice)
    try:
        if EvenGt2(n):
            print(checkGoldbachConjecture(n))
    except LessThanTwoError:
        print("Number has to be greater than two. Try again.")
    except NotEvenError:
        print("Number has to be even. Try again.")
    except:
        print("Something unknown has happened. Try again.")
