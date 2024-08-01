import random

# extracted a unit of functionality so it can be tested much more easily
def evaluateGuess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print("Correct")
            return
    else:
        print("Incorrect")


    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            if evaluateGuess(guess, answer):
                break
        except ValueError:
            print("Please enter a number")
            continue
