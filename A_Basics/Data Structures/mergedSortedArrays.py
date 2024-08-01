array1 = [0,3,4,31]
array2 = [4,6,30]

def mergeSortedArrays(array1, array2):
    merged = array1 + array2
    merged.sort()
    print(merged)

mergeSortedArrays(array1, array2) # prints [0, 3, 4, 4, 6, 30, 31]