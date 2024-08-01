from collections import Counter, defaultdict, OrderedDict

Counter('aabbccdd')  # Counter({'a': 2, 'b': 2, 'c': 2, 'd': 2})
Counter('aabbccdd').items()  # dict_items([('a', 2), ('b', 2), ('c', 2), ('d', 2)])
Counter('aabbccdd').keys()  # dict_keys(['a', 'b', 'c', 'd'])

# defaultdict - allows you to access keys in a dictionary, but you need to get it a callable value
dictionary = defaultdict(lambda: 5, {'a': 1, 'b': 2})
print(dictionary['c'])  # 0
print(dictionary['a'])  # 1


