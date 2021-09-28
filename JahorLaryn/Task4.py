class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} bird can fly.")

    def walk(self):
        print(f"{self.name} bird can walk.")


class NonFlyingBird(Bird):
    def __init__(self, name, ration="burgers"):
        super().__init__(name)
        self.ration = ration

    def fly(self):
        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute 'fly'"
        )

    def eat(self):
        print(f"{self.name} bird eats {self.ration}.")

    def swim(self):
        print(f"{self.name} bird can swim.")


class FlyingBird(Bird):
    def __init__(self, name, ration="eggs"):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        print(f"{self.name} bird eats {self.ration}.")


class SuperBird(FlyingBird, NonFlyingBird):
    def __init__(self, name, ration="milk"):
        super().__init__(name, ration)

    def fly(self):
        Bird.fly(self)

    def eat(self):
        NonFlyingBird.eat(self)

    def __str__(self) -> str:
        return f"Bird {self.name} can walk, fly and swim."
