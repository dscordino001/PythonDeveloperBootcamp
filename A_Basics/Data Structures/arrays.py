strings = ['a', 'b', 'c', 'd']
# 4*4 = 16 bytes of storage is used on a 32 bit system
# 4*8 = 32 bytes of storage is used on a 64 bit system

strings[2] # O(1) - constant time

# append - add something at the end of the array
strings.append('e') # O(1)

# pop - remove the last item
strings.pop() # O(1) - removed "e"

# insert - add something at the beginning of the array
strings.insert(0, 'x') # O(n) - linear time because you have to shift all of
                       # the numbers in memory each time you add a number

# splice - add something in the middle of the array
strings.insert(2, 'alien') # O(n/2)

# remove - remove the first occurrence of an item
strings.remove('b') # O(n) - linear time because you have to shift all of the
                    # numbers in memory each time you remove a number

# index - find the index of an item
index = strings.index('c') # O(n) - linear time because you have to iterate
                           # through the array to find the index

# count - count the number of occurrences of an item
count = strings.count('a') # O(n) - linear time because you have to iterate
                           # through the array to count the occurrences

# sort - sort the array in ascending order
strings.sort() # O(n log n) - time complexity depends on the sorting algorithm

# reverse - reverse the order of the array
strings.reverse() # O(n) - linear time because you have to iterate through the
                  # array to reverse the order

# extend - extend the array by appending elements from another array
other_strings = ['f', 'g', 'h']
strings.extend(other_strings) # O(k) - time complexity depends on the size of
                              # the other array

# clear - remove all elements from the array
strings.clear() # O(1) - constant time

# IMPLEMENT AN ARRAY
# -------------------------------

class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}
    
    get(self, index):
        return self.data[index]

    push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length
    
    pop(self):
        last_item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return last_item

    delete(self, index):
        item = self.data[index]
        self.shift_items(index)
        return item

    shift_items(self, index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length -= 1

# create an instance of the MyArray class
new_array = MyArray()
new_array.push('hi')
new_array.push('you')
new_array.push('!')
new_array.delete(1)
print(new_array)

# create a function that reverses a string
# ----------------------------------------
def reverseAndPrintString(inputString):
    reversedString = inputString[::-1]
    print(reversedString)

reverseAndPrintString("hello") # prints "olleh"



