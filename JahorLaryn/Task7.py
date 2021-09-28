class Money:
    def __init__(self, value, currency="USD"):
        self.currency = currency
        self.exchange_rate = {"EUR": 0.93, "BYN": 3.0, "USD": 1.0}
        self.value = value * self.exchange_rate[currency]

    def __rmul__(self, factor):
        return Money(self.value * factor)

    def __mul__(self, factor):
        return Money(self.value * factor)

    def __add__(self, other):
        if type(other) == int:
            return Money(self.value + other)
        return Money(self.value + other.value)

    def __radd__(self, other):
        return Money(self.value + other)

    def __sub__(self, other):
        if type(other) == int:
            return Money(self.value - other)
        return Money(self.value - other.value)

    def __rsub__(self, other):
        if type(other) == int:
            return Money(other - self.value)
        return Money(other.value - self.value)

    def __truediv__(self, factor):
        return Money(self.value / factor)

    def __str__(self) -> str:
        return f"{self.value} {self.currency}"
