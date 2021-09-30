import time
from contextlib import contextmanager


@contextmanager
def catchtime():
    start = time.time()
    timer = lambda: time.time() - start
    try:
        yield timer
    finally:
        f = open(str(start), "w")
        f.write(str(timer()))


with catchtime() as t:
    time.sleep(1)
print(f"Execution time: {t()} secs")
