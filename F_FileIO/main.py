'''
File Input/Output
- open
    - myFile = open('file', mode)
    - mode: r, w, a, r+, w+, a+
    - print(myFile.read())
    - you can only open and read the file once because the file is read with the cursor
- readlines
    - myFile.readline() - returns the first line
    - myFile.readlines() - returns a list of lines
- you do have to close the files that you open (myFile.close())

- read, write, append
with open('file', 'r+') as myFile: - don't have to close the file
    text = myFile.write('hello')
    print(text) - if there is text already in the file, it will overwrite it
- you commonly work with files in a try-except block

file = open('test.txt')
print(file.read()) # you can only read a file once. the cursor will be at the end of the file
file.seek(0) # this will move the cursor back to index 0
file.close() # you have to close the file when you are done with it
try:
    with open('test.txt', mode='r+') as file: # r+ is read and write, a is append
        text = file.write('hey it is me') # the cursor will reset when you write to a file
        print(file.readlines())
except FileNotFoundError as err:
        print('file does not exist')
        raise err
except IOError as err:
    print('IO error')
    raise err
'''

from translate import Translator
translator = Translator(to_lang='ja')
try:
    with open('test.txt', mode='r') as file:
        text = file.read()
        translation = translator.translate(text)
        print(translation)
    with open('testJa.txt', mode='w') as jaFile:
        jaFile.write(translation)

except:
    pass



