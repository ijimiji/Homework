class MySquareIterator:
    def __init__(self, lst):
        self.arr = lst
        self.current = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < len(self.arr):
            return self.arr[self.current] ** 2
        raise StopIteration
