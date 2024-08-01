import random 


def runGuess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print("Correct")
            return True
    else:
        print("Guess out of range")
        return False

def main():
    answer = random.randint(1,10)
    while True:
        try:
            guess = int(input("Input a Number 1-10: "))
            if (runGuess(guess, answer)) == True:
                break
        except ValueError:
            print("Please Enter a Number")
            continue

if __name__ == '__main__':
    main()