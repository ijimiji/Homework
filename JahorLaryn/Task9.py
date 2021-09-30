class EvenRange:
    def __init__(self, begin, end):
        self.end = end
        if begin % 2 == 0:
            self.current = begin
        else:
            self.current = begin + 1

    def __iter__(self):
        return self

    def __next__(self):
        old_value = self.current
        self.current += 2
        if old_value < self.end:
            return old_value
        raise StopIteration
