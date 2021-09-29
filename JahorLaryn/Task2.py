from contextlib import contextmanager

@contextmanager
def file_open(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()

with file_open("bebra.txt", "r") as f:
    print(f.read())
        
