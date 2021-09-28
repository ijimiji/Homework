class Counter:
    def __init__(self, start=0, end=-1):
        self.counter = start
        self.end = end

    def get(self):
        return self.counter

    def increase(self):
        if self.counter + 1 == self.end:
            raise Exception("Maximal value is reached.")
        else:
            self.counter += 1
