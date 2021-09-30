def endless_fib_generator():
    yield 1
    yield 1
    last = 1
    last_but_one = 1
    while True:
        last, last_but_one = last + last_but_one, last
        yield last


gen = endless_fib_generator()
x = 0
while x < 100:
    x = next(gen)
    print(x)
