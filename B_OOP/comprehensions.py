someList = ['a', 'b', 'g', 'b', 'n', 'b', 'd', 'm', 'n', 'n', 'g', 'q']
print(list(set({itemInList for itemInList in someList if someList.count(itemInList) > 1})))
