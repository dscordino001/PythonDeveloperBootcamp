# create a function that takes a number (index of a fib number) and returns the fibonacci sequence up to that number
def fib(index):
    curr = 0
    next = 1
    result = []
    for i in range(index):
        result.append(a)
        temp = curr
        curr = next
        next = temp + next
    return result


print(fib(15))
