from threading import Thread, Condition
from time import sleep


class Fork:
    def __init__(self):
        self.cond = Condition()
        self.status = True

    def take_fork(self):
        with self.cond:
            while not self.status:
                self.cond.wait()
            self.status = False

    def return_fork(self):
        with self.cond:
            self.status = True
            self.cond.notify()


class Philosopher(Thread):
    def __init__(self, name, left, right):
        Thread.__init__(self)
        self.name = name
        self.left = left
        self.right = right
        self.times = 0

    def think(self):
        print(f"{self.name} is thinking")
        sleep(3)

    def eat(self):
        ending = "time" if self.times == 1 else "times"
        print(f"{self.name} has started eating")
        sleep(10)
        self.times += 1
        print(f"{self.name} has eaten {self.times} {ending}")

    def decide(self):
        while True:
            self.think()
            self.left.take_fork()
            print(f"{self.name} took left fork")
            self.right.take_fork()
            print(f"{self.name} took right fork")
            self.eat()
            self.right.return_fork()
            self.left.return_fork()

    def run(self):
        self.decide()


if __name__ == "__main__":
    thinkers_list = ["Heidegger", "Kierkegaard", "Plato", "Evola", "Sartre"]
    forks = [Fork() for i in range(5)]
    philosophers = [
        Philosopher(f"{thinkers_list[i]}", forks[i], forks[(i + 1) % 5])
        for i in range(5)
    ]
    philosophers[0].start()
    sleep(3)
    for philosopher in philosophers[1:]:
        philosopher.start()
