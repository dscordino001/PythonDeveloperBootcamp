import timeit

# WHAT IS GOOD CODE
#_____________________________________________________________________________________
# create an array called nemo with nemo is the array
nemo = ["nemo"]
everyone = ["dory", "bruce", "marlin", "nemo", "gill", "bloat", "nigel", "squirt", "darla", "hank"]
largeArray = ["nemo" for i in range(10000)]
largeArray.append("dory")

# create a fucntion that loop through the array and print "Found Nemo!" if nemo is found
def findNemo(array):
    for i in range(0, len(array), 1):
        if array[i] == "nemo":
            print("Found Nemo!")
            break # adding the break statement will stop the loop once nemo is found
 
# call the function and pass the array as an argument
def main():
    findNemo(largeArray)

if __name__ == '__main__': 
    start = timeit.timeit()
    main()
    end = timeit.timeit()
    timeToRun = end - start
   #                               {Variable:[alignment][width][,][.precision][type]}
    print(f"Time to Complete Task: {timeToRun:s<7,.5f} seconds")
    
boxes = [0,1,2,3,4,5]

def logFirstTwoBoxes(boxes):
    print(boxes[0])
    print(boxes[1])

logFirstTwoBoxes(boxes)

# this will output 0 and 1 which would give us O(2) complexity,
# but we can simplify this to O(1) because it's constant time

# Log all pairs of array

numbers = [1,2,3,4,5]
arrayPairs = []
lenNum = len(numbers)
for i in range(1,lenNum+1,1):
    for j in range(1,lenNum+1,1):
        arrayPairs.append([i,j])
        j+=1
    i+=1
print(arrayPairs)


def logAllPairsOfArrays(input):
    input = int(input)
    arrayPairs = []
    lenNum = len(numbers)
    for i in range(1,lenNum+1,1):
        for j in range(1,lenNum+1,1):
            arrayPairs.append([i,j])
            j+=1
        i+=1
    print(arrayPairs)

logAllPairsOfArrays(input)


# -------------------------------------------------
# SPACE COMPLEXITY

# the space complexity talks about additional space, so we don't care how big the input is
# within the function, are we adding any space? No, we are just creating an I variable
# so this has space complexity of O(1)
def boo(n):
    for i in range(0, n, 1):
        print("Boo!")

boo(1,2,3,4,5)

# We are just filling out a array n times with hi
# We created a variable and a new array, that is filled with n loops in our function
# We ignore the constant of hiArray (1), so the space complexity is O(n)
def arrayOfHiNTimes(n):
    hiArray = []
    for i in range(0, n, 1):
        hiArray.append("hi")
    return hiArray

arrayOfHiNTimes(6) # returns an array of hi 6 times

# 
# 

