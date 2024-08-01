# def do_stuff(num = 0):
#     try:
#         if num:
#             return num + 5
#         else:
#             return "Please enter number"
#     except ValueError as err:
#         return err

import random

def guessNumber(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print("You are a genius!")
            return
    else:
        print("Hey bozo, I said 1~10")

if __name__ == '__main__':
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input("Enter a Guess Here | Number 1-10 -> "))
            if guessNumber(guess, answer):
                break
        except ValueError:
            print("Please enter a number")
            continue

