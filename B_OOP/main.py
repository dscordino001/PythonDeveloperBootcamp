# this is a class with an object <obj1>
# class BigObject:
# pass

# obj1 = BigObject() # instantiation
# obj2 = BigObject() # instantiation
# obj3 = BigObject() # instantiation


# WIZARD GAME
class PlayerCharacter:
    # class object attribute. static
    membership = True

    # dunder method. self refers to player character.
    # self.name refers to the name of the player character
    # safegaurding the age of the player character
    def __init__(self, name='anonymous', age=0):
        if PlayerCharacter.membership and age > 18:
            self.name = name
            self.age = age
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return 'done'

    # you need to put self.name to access the name of the player character
    def shout(self):
        print(f'my name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Cindy', 25)
player2 = PlayerCharacter('Tom', 30)

print(player1.name)  # Cindy
print(player2.name)  # Tom
player2.attack = 50

print(player1.attack)  # AttributeError: 'PlayerCharacter' object has no attribute 'attack'
print(PlayerCharacter.adding_things(2, 3))  # 5


# Create a Wizard Game to demonstarte the use of classes, objects, and their inheritance
class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')


class Wizard(User):
    def __init__(self, name, power, email):
        self.name = name
        self.power = power
        # this allows you to get the email attribute from the User class
        super().__init__(email)

    def attack(self):
        # shows the attack method of the User class
        User.attack(self)
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    # attack is a shared name between the Wizard and Archer classes, but they do 2 different things
    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')


# multiple inheritance
class Hybrid(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)


wizard1 = Wizard('Merlin', "hotguy@hotmail.com", )
archer1 = Archer('Robin', 100)
wizard1.attack()
hb1 = Hybrid('Robin', 50, 100)
hb1.attack()

# to check if an object is an instance of a class, use isinstance()
# isinstance(object, class)
print(isinstance(wizard1, User))  # True
print(isinstance(wizard1, object))  # True


def player_attack(character):
    character.attack()


# two different objects were passed in, so you get 2 different outputs
player_attack(wizard1)  # attacking with power of 50
player_attack(archer1)  # attacking with arrows: arrows left - 100


# Dunder Methods
class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    # dunder method that modified the behavior of the object and the str dunder method
    def __str__(self):
        return f'{self.color}'

    # dunder method
    def __len__(self):
        return 5

    # dunder method
    def __call__(self):
        print('you called me?')

    def __getitem__(self, index):
        # returns the value of the key in the dictionary
        return self.my_dict[index]


action_figure = Toy('red', 0)
# allows you to use action_figure like you would if you just used str(action_figure)
# this now returns the color of the action figure. it's only modified when you use it on the specific object
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())  # deletes a variable that you have in your program
# uses __getitem__ to get the value of the key in the dictionary
print(action_figure['name'])  # Yoyo


# Pure Functions - li is for list
def multiply_by2(li):
    # if this was put outside of the function, it would be a side effect
    new_list = []
    for item in li:
        new_list.append(item * 2)
    # if this was changed to return print(new_list),
    # it would be an impure function because it prints to the display
    return new_list


multiply_by2([1, 2, 3])  # [2, 4, 6]
# nothing in the outside is affected by the function

# Lambda Expressions
from functools import reduce

my_list = [1, 2, 3]


def multiply_by2(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 0))
print(my_list)
# you don't need to define multiply_by2 as a function
# takes an item from list, multiplies it by 2, and returns it
print(list(map(lambda item: item * 2, my_list)))  # [2, 4, 6]
print(list(filter(lambda item: item % 2 != 0, my_list)))  # [1, 3]
print(reduce(lambda acc, item: acc + item, my_list))  # 6
