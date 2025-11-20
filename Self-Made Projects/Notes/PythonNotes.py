#This is a comment.

''' 
This is a multi-line comment.
'''

#Unlike Java, you do not need to declare variable types, nor do you need semicolons, or a main method.
myInt = 80
myString = "Hello World!"
StringA, StringB = "Hello", "World"
myMultiLineString = """Oh
Wow
Neat"""

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

#You can also format strings, using curly brackets {} and str.format or f
name = 'Victor'
age = 19
print("I am {}, I am {} years old".format(name, age))
print(f"I am {name}, I am {age} years old")

'''Separators, too to change the ending'''
print("A", sep = " ")
print("B")

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
<String>.split(a) - splits into list of strings with separator a - more on lists later
<String>.replace(a, b) - replaces a with b

<String>[4:8] - returns substring from 4 to 8
<String>[4] - returns character at 4
<String>[:8] - returns substring to 8
<String>[4:] - returns substring from 4
<String>[4:8:6] - returns substring from 4 to 8, skips 6

You can even use negative numbers for the above 5, counting from the end of the string

<String>[::-1] - reverses the string
'''

#Lists are like ArrayLists in Java, with some differences of course.
myList = list()
myList = []
myList.append(3)
myList = [1, 2, 3]

'''
<List>.append() - adds to end of list
<List>.insert(index, item) - adds to index of list
<List>.remove() - removes item
<List>.pop() - removes item at index, or last item for nothing
<List>.clear() - deletes all elements of the list
<List>.copy() - copies all elements of the list so no changes are made to original
<List>.sort() - sorts list in ascending order, use "reverse=true" for descending
<List>.extend() - adds list to end of list, or you could use +
<list>[] - access to element of list, or slices elements

Methods also used from string: 
count()
index()
reverse()

You can also use negative indexes to access items!
Use the keyword "in" to check if an item is in a list
Use the keyword "Del" to delete an index, or the entire list

You can unpack lists by setting variables equal to the list
'''
a, *b = myList
print(a)

'''
You can also do the opposite, packing them to account for an unknown number of items
'''

def sum_all(*nums):
    ret = 0
    for i in nums:
        ret += i
    return ret

'''
We use enumerate to check the index of an item in a list
'''

for index, item in enumerate([20, 30, 40]):
    print(index, item)

'''
Lists can be combined through zip
'''
odds = [1, 3, 5, 7, 9]
evens = [0, 2, 4, 6, 8]
topRow = []
for i, j in zip(odds, evens):
    topRow.append(j, i)

#List Comprehension is another way to change things into a list

ExampleString = 'Language'
lst = [i for i in ExampleString]

'''
Can also use if statements inside
'''

numbers = [i for i in range(5) if i%2 == 0]
print(numbers)

'''
Or to flatten lists - keep in mind the multiple for statements
'''

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]

#Condition statements are the same as java, e.g. ==, >, <, >=, <=
if 3 in myList:
    print("3 is in myList")
elif len(myList) > 0:
    print("Something is in myList")
else:
    print("MyList is empty.")

'''
The "in" operator is used to check if things are in lists
The "is" operator is used to check if two varaibles refer to the same object
The "not" operator is the inverse of "is"

If you want to use && and ||, just type "and" or "or"

If you haven't noticed, python checks for "code blocks", or tabs and indentations in place of brackets {}
'''

#Loops are relatively unchanged, though for loops are replaced with for:each.
'''
Range() takes 3 arguments but defaults to range(end). 
Usually, Range(start, stop, increment)
Range stops at 1 before stop.
There's also for:else, which does the else when the loop ends.
When a statement is required after a colon, but we don't want to execute any code, we can use the word pass.
'''
for x in range(5):
    print(x)
for x in myList:
    print(x)
for x in myList:
    pass

'''Loops include break and continue conditions.
Continues skip the current iteration and continue with the next.'''
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

print_string()

def add_three(a, b, c):
    return a+b+c

def add_many(*aa):
    total = 0
    for a in aa:
        total += a
    return total

def nestedFunction(f, x):
    return f(x)

'''
Functions return None by default
Remember as well default parameters when we don't pass arguments
Otherwise, functions remain relatively unchanged. You can choose if you want to return or not
They are like OCaml functions, where they can be taken as arguments and returned. Notable functions include:
    map(f, x) - applies function f to x
    filter(f, x) - returns values that return True when f is applied
    reduce(f, x) - applies f to x but returns a single value, like List.fold() in OCaml
THESE RETURN ITERATORS, not lists, so enclose with list() to convert.
Closures apply as well
'''

#Lambda Functions are anonymous functions.

addThree = lambda a, b, c: a + b + c
trueOrFalse = lambda arg: True if arg >= 1 else False

'''
To invoke a lambda in print, encapsulate with parentheses
'''

print((lambda a,b: a+b)(2,3))

#Decorators add a new functionality to an existing object.

'''
uppercase_decorator takes a function, then turns the string output of the function into uppercase.
'''

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

'''
The important part.
'''

@uppercase_decorator

def greeting():
    return 'Welcome to Python'
print(greeting())

#Sorted() can be applied to any datatype. Keep in mind python sorting is always ascending.

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sortedTuples = sorted(student_tuples, key=lambda student: student[2])

'''
where
sorted(iterable, key=None, reverse=false)
is the default
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
del <Dictionary>[key] removes a key, value pair by taking a key
<Dictionary>.pop(key) is the same concept, but returns the value

If we try <Dictionary>[key] for a key that doesn't exist, we get an error
instead, do <Dictionary>.get(key)

Add or modify a pair by doing <Dictionary>[key] = value

To change Dictionary to a list of tuples, do <Dictionary>.items()

.copy(), .clear() do the same things we do
<Dictionary>.keys() returns a list of keys, the same thing with .values()
'''

#Tuples are an immutable, ordered collection of data 

planets = ("Earth", "Jupiter", "Mars", "Saturn")
PlanetList = list(planets)

#Remember list unpacking? here's that for tuples and dictionaries.

Ea, Ju, *P = planets

numA, *nums = phonebook.values()
def printPhone(name, number):
    print(name + number)
printPhone(**phonebook)

'''
Packing also applies here.
'''

def printPhoneInfo(**phones):
    for key in phones:
        print(f"{key} = {phones[key]}")

#Sets are like tuples, but unordered. Items are immutable, and you can add and remove in sets. No duplicates allowed.

numbers = {3.12, 5.22, 9.14, 2.1}
numbers.add(9.4)
numbers.update({3.3, 9.9})

if (3.12 in numbers): 
    numbers.discard(3.12) #Discard is the same as remove, but no raising errors.

numbers.clear()
PlanetSet = set(PlanetList)

'''
Advanced Set Functions
<Set>.intersection(set) - returns the set of items in Set U set
<Set>.issubset(set) - returns boolean if Set is subset of set
<Set>.issuperset(set) - returns boolean if Set is superset of set
<Set>.difference(set) - returns difference of Set and set
<Set>.symmetric_difference(set) - returns symmetric difference of Set and set
'''

#Modules in Python are like java class files, with the exception that you have to import them.

'''
You could do:
import draw as dra
from dra import draw_game
import *, to import all
When you import functions, you no longer need to do module.function, instead only needing function

You can also tell python where to find modules
PYTHONPATH=/code
sys.path.append("/code")

You can create a function in a different python file and import it as a module
'''

#os is a module designed to interact with the operating system



#sys is a module designed to interact with python runtime environment



#statistics is a self-explanatory module

from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3

#math, like java's math has some interesting functions

import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base

#string is a module that has some variations and functions on strings

import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

#random is surprisingly not located in math

from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive

#datetime is a specific module to handle dates and times.

from datetime import datetime
now = datetime.now()
print(now)

'''
Instead of f, we can use strftime to format datetime
'''

time_now = now.strftime("%m/%d/%Y, %H:%M:%S")
print(time_now)

'''
strptime is String to Time
'''

Dobject1 = datetime.strptime("September 21, 1987", "%B %d, %Y")
print(Dobject1)

'''
date(y,m,d) gives a date object
'''

from datetime import date
Dobject2 = date(2006, 1, 6)
print(Dobject2)

'''
time(h,m,s,ms) gives time
You can subtract times as well by subtraction or using timedelta.
'''

from datetime import time
Tobject1 = time(10,30,30)

from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)

#Regex is located in module re

import re

'''
re.match(substring, string, flags) - Searches start of string and returns matched objects
    .span() - gives the indeces for where substring is located in string
    flags include re.IGNORECASE, etc
        re.I - include all cases
re.search(substring, string, flags) - Searches all throughout the string
re.findall(substring, string, flags) - returns all the matched objects in string as a list
re.split(substirng, string, flags) - Takes a string, splits it at the match points, returns a list
re.sub(substring, replacement, string, flags) - Replaces one or many matches within a string

If we want to account for extra cases, we use these identifiers in regex, as r"identifier"
    [A-Za-z0-9] - accepts chars in set, e.g. [Aa]pple accounts for Apple and apple
    \ - special characters, where \d is only digits and \D is no digits
    . - any character except \n
    ^ - starts with, e.g. r"^abc" means a string that starts with abc and r"[^abc]" means any string that doesn't
    $ - ends with
    * - 0 or more times
    + - 1 or more times
    ? - 0 or 1 time
    () - number of characters allowed, e.g. (3) is exactly 3 and (3,8) is between 3 and 8, with (3,) meaning at least 3
    | - or
'''

#You can read files in Python, just like java

'''
open(filename, mode)
    mode - 
        r - default, reads file, returns error if dne
        a - appends items to file, or creates if dne
        w - writes to file, or creates if dne
        x - creates a file, returns error if file exists
        t - text mode
        b - binary mode
file.close() - needed after file is done with
    could also do "with as" to close after done using it
file.read(number) - takes the entire text as string
    number - optional, int that limits length of read
    .splitlines() - splits the string by line into list
file.readline() - reads only the first line
file.readlines() - reads all text by lines and returns list
'''

#Packages are directories with a __init__.py file, and can decide which modules are internal.

'''
__init__.py:

__all__ = ["bar"]
'''

#Errors raised in python:
'''
SyntaxError - Wrong syntax usage / character usage for code
NameError - Undefined variables
IndexError - Going out of bounds for iterables
ModuleNotFoundError - Module name is misspelled
AttributeError - Function does not exist in module or is misspelled
KeyError - Key:value pair does not exist in dictionary
TypeError - Wrong type usage
ImportError - Function does not exist in module or is misspelled
ValueError - Changing type for a value whose type cannot be changed 
ZeroDivisionError - Dividing by zero
'''

#Exceptions are for when code brings up errors, with the general format being:
try:
    print(10 + '5')
except TypeError:
    print("10" + 5)
else: 
    print(10 + "5")
finally: 
    print("Error")

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