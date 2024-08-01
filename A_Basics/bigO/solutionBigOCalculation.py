def funChallenge(input):
    a = 10 # O(1) - assingment
    a = 50 + 3 # O(1) - assignment

    for i in range(len(input)): # O(n) - loop will run n times. Linear times
        anotherFunction() # O(n) - function will run n times
        stranger = True # O(n) - assignment will run n times
        a += 1 # O(n) - assignment will run n times
    return a # O(1) - return statement happens once

funChallenge()

#3 steps + n + n + n + n
#Big O = (3 + 4n)
# gets simplified to O(n)
