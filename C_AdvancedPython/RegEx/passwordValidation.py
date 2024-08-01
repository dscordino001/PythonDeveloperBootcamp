import re

# 8+ charachers long
# contain any sort of letters, numbers, $%#@
# has to end with a number

pattern = re.compile(r'^[\w@#$%]{8,}.+[0-9]$')
passwordToTry = ("jdsfskjfgsdkl!g%234498#")
print(pattern.fullmatch(passwordToTry))
