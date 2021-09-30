class MyNumberCollection:
    def __init__(self, *args):
        self.arr = []
        self.current = -1
        for arg in args:
            if type(arg) == int or type(arg) == float:
                self.arr.append(arg)
            else:
                raise ValueError

    def __str__(self):
        return str(self.arr)

    def __iter__(self):
        return self

    def next(self):
        self.current += 1
        if self.current < len(self.arr):
            return self.arr[self.current]
        raise StopIteration

    def __getitem__(self, i):
        return self.arr[i] ** 2

    def __add__(self, other):
        return MyNumberCollection(*(self.arr + other.arr))
