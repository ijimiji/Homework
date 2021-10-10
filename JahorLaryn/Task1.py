from multiprocessing import Process
from asyncio import sleep

def wittgenstein():
    pass

def heidegger():
    pass

def socrates():
    pass

def kierkegaard():
    while True:
        print("1")
        sleep(100)

def decartes():
    while True:
        print("0")
        sleep(100)

def main():
    forks = {
        1: "available",
        2: "available",
        3: "available",
        4: "available",
        5: "available",
    }
    processes = [
        Process(target=decartes),
        Process(target=kierkegaard)
    ]
    for process in processes:
        process.start()

if __name__ == "__main__":
    main()