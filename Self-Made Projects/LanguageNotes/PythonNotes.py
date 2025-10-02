#This is a comment.

''' 
This is a multi-line comment.
'''

#Unlike Java, you do not need to declare variable types, nor do you need semicolons, or a main method.
myInt = 80
myString = "Hello World!"
'''
Variables cannot start with numbers.
They cannot have symbols except underscore _.
Variable names are case-sensitive.
'''

#Like C, putting variables in print statements requires output operators.
print("I am going to say %s" % myString)

'''
%s - strings
%d - ints
%f - floats

%.<# of digits>f - floating point rounded to a place
%x - ints, in lowercase hex
%X - ints, in uppercase hex
'''

#Remember Java's String methods? Some of those apply here.
print(myString.index("e"))

'''
len(<String>) - returns length
<String>.index() - returns index of caracter
<String>.count() - returns number of specified character
<String>.upper() - Java's .toUpperCase()
<String>.lower() - Java's .toLowerCase()
<String>.startswith() - checks if the start of the string contains it
<String>.endswith() - checks if the end of the string contains it
<String>.split() - splits into list of strings - more on lists later

<String>[4:8] - returns substring from 4 to 8
<String>[4] - returns character at 4
<String>[:8] - returns substring to 8
<String>[4:] - returns substring from 4
<String>[4:8:6] - returns substring from 4 to 8, skips 6

You can even use negative numbers for the above 5, counting from the end of the string

<String>[::-1] - reverses the string
'''

#Lists are like ArrayLists in Java, with some differences of course.
myList = []
myList.append(3)
myList = [1, 2, 3]

'''
<List>.append() - adds to end of list
<list>[] - access to element of list
'''

#Condition statements are the same as java, e.g. ==, >, <, >=, <=
if 3 in myList:
    print("3 is in myList")

'''
The "in" operator is used to check if things are in lists
The "is" operator is used to check if two varaibles refer to the same object
The "not" operator is the inverse of "is"

If you want to use && and ||, just type "and" or "or"

If you haven't noticed, python checks for "code blocks", or tabs and indentations in place of brackets {}
'''

#Loops are relatively unchanged, though for loops are replaced with for:each.
for x in range(5):
    print(x)
for x in myList:
    print(x)

'''While loops include break and continue conditions.'''
x = 0
while True:
    print (x)
    x+=1
    if x >= 5:
        break

'''While loops can also have else statements, like ifs'''
x = 0
while x < 5:
    print (x)
    x+=1
else:
    print("oh noes")

#Function syntax requires "def", the name, parentheses for inputs, and a colon.
def print_string():
    print("Yuh")

'''
Otherwise, functions remain relatively unchanged. You chan choose if you want to return or not
'''

#Classes are relatively simple, the concepts are the sane as java.
class TestClass:
    def __init__(self):
        pass
    def add(a, b):
        return a+b
    def test(self):
        print("Go")

'''
Apparently if you want a function to be called when the class is initiated, use __init__
'''

#Dictionaries are pretty much just hashmaps. Key value pairs and whatnot.
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

'''
del <Dictionary>[] removes a key, value pair by taking a key
<Dictionary>.pop() is the same concept
'''

#Tuples are an ordered collection of data that cannot be modified in length.

planets = {
    "Earth"
    "Jupiter"
    "Mars"
    "Saturn"
}

#Sets are like tuples, but unordered.

numbers = {
    3.12,
    5.22,
    9.14,
    2.1
}

#Modules in java are like java class files, with the exception that you have to import them.

'''
You could do:
import draw
form draw import draw_game
import *, to import all

You can also tell python where to find modules
PYTHONPATH=/code
sys.path.append("/code")
'''

#Packages are directories with a __init__.py file, and can decide which modules are internal.

'''
__init__.py:

__all__ = ["bar"]
'''

#The input() method receives an input, but does not know what type of variable it is.
num = int(input())
print(num)
decimalnum = input()
decimalnum = float(input())
print(decimalnum)

#Virtual Environments protect your system, and kind of works like Docker.
'''
On Linux, make sure to do
python3.12 -m venv [name]
source [name]/bin/activate
to run the virtual environment, and
deactivate
to exit out.
'''

#Like Ocaml, python can be run in the shell.
'''
Similar function, Ctrl+D or
exit()
to exit.
'''

#Built-in Functions.
'''
Python has a lot of built-in functions, make sure to know the important ones.

print() - Print out 
len() - counts number of characters
type() - check the type of data
str() - converts number to string
int() - converts string to number, e.g. "10"
float() - converts integer to decimal

These take a list as a value
min() - minimum value
max() - maximum value
sum() - returns sum

help() - gives information, will give functions. Press Q to exit.
'''

#Lesser known operations.
pyth = 5 // 2
print(pyth)

on = 3**2
print(on)

'''
// is floor division, which removes the remainder/rounds down. Python shell treats numbers not like ints.
** is exponentials
'''