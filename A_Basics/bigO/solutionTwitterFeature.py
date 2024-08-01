# Function that returns their newest and oldest tweet
# find 1st and nth tweets, but we don't know how twitter stores this
# if the tweets are in an array...

array = ['hi', 'my', 'teddy', 'bear', 'is', 'cute']
array[0] # O(1)
array[len(array)] # O(1)

# because we are comparing each element to each other, we have a nested loop
# O(n^2)
# this is expensive so we might have to store this another way that's more efficient

class Tweet:
    def __init__(self, content):
        self.content = content

array = [Tweet('hi'), Tweet('my'), Tweet('teddy'), Tweet('bear'), Tweet('is'), Tweet('cute')]

# what is the space complexity of this:
# 'sbfoadscbrburvbuhkb'.length ###treat this as javascript. its O(1) because .length is a lookup, it's not a method
