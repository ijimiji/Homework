a = "I am global variable!"

def enclosing_funcion():
    a = "I am variable from enclosed function!"
    def inner_function():
        a = "I am local variable!"
        print(a)

# Subtask 1
from types import CodeType, FunctionType
for item in enclosing_funcion.__code__.co_consts:
    if isinstance(item, CodeType) and item.co_name == "inner_function":
        FunctionType(item, globals())()
