# this is the same as list(range(100))
def makeList(num):
    result = []
    for i in range(num):  # range(num) is a generator. It doesn't store all the values in memory
        result.append(i * 2)
    return result  # this result will live in memory


myList = makeList(100)  # points to a location in memory, taking up space
print(myList)


# defining our own generator
def generatorFunction(num):
    for i in range(0, num, 1):
        yield i * 2  # yield is a keyword that returns a value and pauses the function

# this would throw an error because next gets called more times that the generator has values
g = generatorFunction(2)
#g = generatorFunction(100) will work
next(g)
next(g)
print(next(g))  # 4 because we ran through the generator twice and only keeps the most recent value in memory
print(next(g)) # 6 because we ran through the generator three times

# new example --------------------------------------------
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
    # for i in list(range(100000000)): will take longer because list stores all the values in memory
    for i in range(100000000):
        i*5

long_time()  # this will return the time it took to run the function

# new example --------------------------------------------
def specialFor(iterable):
    iterator = iter(iterable) # iter makes the iterable into an iterator
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break

specialFor([1,2,3])  # this loops through iterable objects using next in the same memory spot
# create your own range function
class MyGenerator():
    # accumulator for what iteration you are on
    current = 0
    def __init__(self, first, last): # this mimics a range function
        self.first = first
        self.last = last
    # use dunder methods iter to make the class iterable
    def __iter__(self):
        return self
    # use dunder methods next to let the class know what to do when next is called
    def __next__(self):
        # you need a state to keep track of where you are in the generator
        if MyGenerator.current < self.last:
            # return the current value and increment the current value
            num = MyGenerator.current
            MyGenerator.current += 1
            return num
        # raise this iteration because there will be no more things to iterate over
        raise StopIteration

gen = MyGenerator(0, 101)
for i in gen:
    print(i)