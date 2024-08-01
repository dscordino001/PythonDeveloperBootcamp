# 1. print the square of each item in the list
my_list = [5, 4, 3]
print(list(map(lambda item: item ** 2, my_list)))

# 2. list sorting: sort this list based on the second value in the integer pair
myList = [(0, 2), (4, 3), (9, 9), (10, -1)]

print(list(sorted(myList, key=lambda item: item[1])))

