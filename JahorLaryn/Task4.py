a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():
        # Task 2.1
        print(globals()["a"])
        # Subtask 2.2
        nonlocal a
        print(a)
        a = "I am local variable!"
        print(a)

    # Task 1
    return inner_function


inner_function = enclosing_funcion()
inner_function()
