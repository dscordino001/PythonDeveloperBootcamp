# example of a decorator

def my_decorator(a_function):  # this is a function
    def wrapper():  # that wraps another function
        a_function()  # and enhances it
    return wrapper
@my_decorator  # this one lines boosts the function below
def hello():
    print("Hello")
@my_decorator
def bye():
    print("Bye")

hello()
bye()
# hello2 runs the hello function with the decorator
hello2 = my_decorator(hello)
hello2()
# -----------------------------------------
# you can change this function to take a parameter by adding a parameter to the wrapper function
def my_decorator2(a_function):
    def wrapper(x):
        a_function(x)
    return wrapper

@my_decorator2
def hello3(greeting):
    print(greeting)

hello3("Hello")

# create a code performance decorator that times the function

from time import time
def performance(function_accepted):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = function_accepted(*args, **kwargs)
        t2 = time()
        print(f"It took {t2-t1} seconds to run")
        return result

@performance
def long_time():
    for i in range(100000000):
        i*5

long_time()  # this will return the time it took to run the function

