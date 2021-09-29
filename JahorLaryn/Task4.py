def ignore_exceptions(f):
    def wrapper(*args):
        try:
            f(*args)
            print("Yay! Everything is ok.")
        except:
            pass
    return wrapper

@ignore_exceptions
def do_dangerous_stuff(x):
    print(1/x)

do_dangerous_stuff(0)
do_dangerous_stuff(1)