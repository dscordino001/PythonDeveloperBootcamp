'''
# Program that calculates your age 
birthYear = int(input("What year you were born")) # Prompt the user to enter their birth year
birthMonth = int(input("What month you were born")) # Prompt the user to enter their birth month
birthDay = int(input("What day you were born")) # Prompt the user to enter their birth day

if (0 < birthMonth <= 4): # Check if the birth month is between 1 and 4 (inclusive)
    age = 2024 - birthYear # Calculate the age by subtracting the birth year from 2024
elif birthMonth == 5: # Check if the birth month is 5
    if birthDay > 10: # Check if the birth day is greater than 10
        age = 2023 - birthYear # Calculate the age by subtracting the birth year from 2023
    else: # If the birth day is not greater than 10
        age = 2024 - birthYear # Calculate the age by subtracting the birth year from 2024
elif (5 < birthMonth < 13): # Check if the birth month is between 6 and 12 (inclusive)
    age = 2023 - birthYear # Calculate the age by subtracting the birth year from 2023
else: # If none of the above conditions are met
    print("Error: Invalid Input") # Print an error message

print(f"you are {age} years old") # Print the age of the user


# Program that checks your passcode
username = str(input("Enter your username: "))
password = str(input("Enter your password: "))

passwordStars = "*" * len(password)

print(f"Hey {username}, your password {passwordStars} is {len(password)} characters long!")\

# List Methods

basket = [1, 2, 3, 4, 5]
newList = basket.append(100) # Append method adds the value to the end of the list
print(basket) # Output: [1, 2, 3, 4, 5, 100]
print(newList) # Output: None - this is because you have to append before you assign
basket.append(101)
megaNewList = basket
print(megaNewList) # Output: [1, 2, 3, 4, 5, 100, 101]

# Conditional Logic
isOld = True
isLicensed = True

if isOld and isLicensed:
    print("Good to Drive")


# List Slicing
amazonCart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

amazonCart[0] = 'laptop' # Change the first item in the list to 'laptop'
newCart = amazonCart[:] # Copy the list and make a new list
newCart[0] = 'gum' # Change the first item in the copied list to 'gum'
print(amazonCart) # Output: ['laptop', 'sunglasses', 'toys', 'grapes']
print(newCart) # Output: ['gum', 'sunglasses', 'toys', 'grapes']


zapposCart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

zapposCart[0] = 'laptop' 
newZapposCart = zapposCart 
newZapposCart[0] = 'gum' 
print(zapposCart)
print(newZapposCart)

#These 2 lists have the exact same output of ['gum', 'sunglasses', 'toys', 'grapes'] 
#because when you assign a list to another list, you are not creating a new list, 
#you are just creating a reference to the original list. So when you change the referenced list, 
#you are also changing the original list because you point to the same place in memory.


# Logical Operator

isMagician = False
isExpert = True

if isMagician and isExpert:
    print("You are a master magician")
elif isMagician and not isExpert:
    print("At least you are getting there")
elif not isMagician:
    print("You need magic powers")

# Counter that counts up the items in your list
myList = [5,4,3,2,1] 
total = 0
for item in myList:
    total = total + item
print(total)



# simulate a GUI. loop through the list of lists and print out nothing if you see a 0 and print out a * if you see a 1
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

fill = "*"
emptySpace = " "

for row in picture:
    for pixel in row:
        if pixel:
            print(fill, end='') # end='' is used to print on the same line 
        else:
            print(emptySpace, end='') # you need the space there so the pixels print in the right place
    print('') # this is used to print on a new line after each row
    


# exercise: check for duplicates in a list

myList = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicateList = []
for item in myList:
    if myList.count(item) > 1:
        if item not in duplicateList:
            duplicateList.append(item)

print(duplicateList)        

# Define a nested function

def sum(num1, num2):
    def anotherFunc(n1, n2):
        return n1 + n2
    return anotherFunc(num1, num2)

total = sum(10,20)
print(total) 

# create highestEven function that returns the highest even number in a list
'''
def highestEven(list):
    evens = []
    for number in list:
        if number % 2 == 0:
            evens.append(number)
    return max(evens)

print(highestEven([10,2,3,4,8,11]))
