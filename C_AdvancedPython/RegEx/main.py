'''
regex
-------------------------------------------
- RegEx is useful especially for advanced string patterns
regex101.com is a great tool to test your regex patterns
'''

import re
string = "string inside of this text"
pattern = re.compile(r"([a-zA-Z]).(a)") # r is for raw string
b = re.search("this", string) # same as pattern.search(string)
a = pattern.search(string) # gives you a match object that tells you about what/where you found
print(a.span())
print(a.end())
print(a.start())
print(a.group()) # useful when trying multiple searches
print(pattern.findall(string)) # returns a list of all the matches
print(pattern.fullmatch(string)) # returns None because it doesn't match the full string
print(pattern.match(string)) # returns a match if the pattern is at the beginning of the string


