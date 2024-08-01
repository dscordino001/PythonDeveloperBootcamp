import utility
from modulesInPython.shopping.moreShopping.shoppingCart import buy

if __name__ == "__main__":
    print(utility.multiply(2, 3))
    print(buy('apple'))


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('********')
        func(*args, **kwargs)
        print('********')

    return wrapper


@my_decorator
def hello(greeting="youre gay", emoji=':)'):
    print(greeting, emoji)

hello()
hello("poopybumbumMcStinkys")
hello("poopybumbumMcStinkys", ":((((((((((((")

