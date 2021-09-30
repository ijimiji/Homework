import sys


class Open:
    def __init__(self, filename, mode):
        try:
            self.file = open(filename, mode)
        except:
            print("Unexpected error while opening file:", sys.exc_info()[0])
            raise

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        try:
            self.file.close()
        except:
            print("Unexpected error while closing file:", sys.exc_info()[0])
            raise

    def read(self):
        try:
            return self.file.read()
        except:
            print("Unexpected error while reading file:", sys.exc_info()[0])
            raise


with Open("bebra.txt", "r") as f:
    print(f.read())
