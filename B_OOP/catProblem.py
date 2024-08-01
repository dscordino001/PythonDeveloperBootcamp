# Given the below class:
# 1 Instantiate the Cat object with 3 cats
# 2 Create a function that finds the oldest cat
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
# Define a class named Cat
class Cat:
    # Set a class attribute 'species' to 'mammal'
    species = 'mammal'

    # Define the initializer method that gets called when a new object is created from the Cat class
    def __init__(self, name, age):
        # Set the instance attribute 'name' to the value passed as the name parameter
        self.name = name
        # Set the instance attribute 'age' to the value passed as the age parameter
        self.age = age


# Create an instance of the Cat class with name 'Tom' and age 5, and assign it to the variable cat1
cat1 = Cat('Tom', 5)
# Create an instance of the Cat class with name 'Cindy' and age 7, and assign it to the variable cat2
cat2 = Cat('Cindy', 7)
# Create an instance of the Cat class with name 'Cathy' and age 2, and assign it to the variable cat3
cat3 = Cat('Cathy', 2)


def findOldestCat(*args):
    return max(args)


oldestCatAge = findOldestCat(cat1.age, cat2.age, cat3.age)
# Print a formatted string that includes the result of calling
# the find_oldest_cat function with the ages of cat1, cat2, and cat3
print(f"The oldest cat is {oldestCatAge} years old")
