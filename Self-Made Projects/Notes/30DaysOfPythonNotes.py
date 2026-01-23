#Day 1 - Introduction
  

#Day 2 - Variables, Built-in Functions


#Day 3 - Operators


#Day 4 - Strings


#Day 5 - Lists


#Day 6 - Tuples


#Day 7 - Sets


#Day 8 - Dictionaries


#Day 9 - Conditionals


#Day 10 - Loops


#Day 11 - Functions


#Day 12 - Modules


#Day 13 - List Comprehension


#Day 14 - Higher Order Functions


#Day 15 - Python Type Errors


#Day 16 - Python Date Time


#Day 17 - Exception Handling


#Day 18 - Regular Expressions


#Day 19 - File Handling


#Day 20 - Python Package Manager
'''
Python Package Manager, or PIP (Preferred Installer Program), installs python packages
Commands:
    pip --version
    pip install [NAME]
    pip uninstall [NAME]
    pip list
        see the installed packages on the machine
    pip show [NAME]
        see the info about a package
        --verbose adds more details
    pip freeze 
        installed packages with versions

To get read data from a website or API, we can use a package called requests
Methods:
    requests.get()        
        opens network and fetches data from url, returns {RESPONSE} Object
    {RESPONSE}.status_code
        returns status of object, success, failure, etc.
    {RESPONSE}.headers
        checks header types
    {RESPONSE}.text
        extracts text from {RESPONSE}
    {RESPONSE}.json
        extracts json from {RESPONSE}
    {RESPONSE}.content
        extracts bytes from {RESPONSE} 

Methods Example
'''

import requests
url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'
response = requests.get(url)
print(response)
#print(response.status_code)
#print(response.headers) 
#print(response.text)

'''
Package Creation
    A package is a folder that contains one or more module files, each with multiple objects
    see "mypackage"

Further Packages to Know
    Databases
        SQLAlchemy, SQLObject
    WebDev
        Django, Flask
    HTML Parser
        Beautiful Soup, PyQuery
    XML Processing
        ElementTree
    GUI
        PyQt, TkInter
    Data Science
        Numpy, Pandas, SciPy, Scikit-Learn, TensorFlow, Keras
    Networking
        Requests
'''

#Day 21 - Classses and Objects
'''
Python is object-oriented, like Java
    OOP Recap: 
    Classes are constructors of objects
    Objects can have methods
    Default methods are viable, where the variable is already defined in function line
    Getters and Setters
'''

class person:
    def __init__ (self, name='empty'):
        self.name = name
p = person('Victor')
print(p.name)

#Day 22 - Web Scraping
'''
Web scraping is the collection of data from a website and storing it on a local machine or database
We use BeautifulSoup4 and requests to scrape

BeautifulSoup Example
'''

import requests
from bs4 import BeautifulSoup

url2 = 'https://archive.ics.uci.edu/dataset/320/student+performance'
response2 = requests.get(url)
content = response2.content
soup = BeautifulSoup(content, 'html.parser')
print(soup.title)
#print(soup.title.get_text())
#print(soup.body)
#print(response2.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
#table = tables[0]
#for td in table.find('tr').find_all('td'):
    #print(td.text)


#Day 23 - Virtual Environment
'''
Virtual environments create isolated environments so that we don't have dependency conflicts across projects

On Bash, make sure to do
python -m venv [NAME]
source [NAME]/bin/activate
to run the virtual environment, and
deactivate
to exit out.
'''

#Day 24 - Statistics
'''
To analyze data, we have statistics and numpy
numpy is good for working with arrays, which are different from python lists
Methods:
    numpy.array(List, [OPT]dtype={TYPE}, [OPT]order=)
        Creates a numpy array from a list
        Datatype can be changed to float, bool, str, etc.
        Order:
            C - Row-major order, which is default
            F - Column-major order
            A - Any order, numpy chooses between C or F based on the most efficient
            K - Keep order, when creating a new array from an existing one
    numpy.zeros(List, [OPT]dtype={TYPE}, [OPT]order=)
    numpy.ones(List, [OPT]dtype={TYPE}, [OPT]order=)
        Creates arrays of solely zeroes or ones

    {ARRAY}.tolist() 
        Turns numpy array to list
    {ARRAY}.shape
        Gives the dimensions of the numpy array
    {ARRAY}.dtype
        Gives the datatype of the numpy array
    {ARRAY}.size
        Gives the number of items in the numpy array
    {ARRAY}.reshape({SIZE})
        Reshapes the array into a valid A x B x C x ... array
    {ARRAY}.flatten()
        Flattens the array into a 1-Dimensional array
    {ARRAY}.hstack({ARRAY}, {ARRAY})
    {ARRAY}.vstack({ARRAY}, {ARRAY})
        Appends arrays to each other horizontally or vertically
    {ARRAY}.itemsize
        checks the size of an array in bytes

You can also use operations on arrays, which affect all items in the array
You can also convert array datatype
You can slice arrays like lists

Numpy also has random numbers
Methods:
    numpy.random.random({INT})
        Generates a list of {INT} random floats, default single random number
    numpy.random.randint({INT},{INT}, [OPT]size={SIZE})
        Generates one random int between two ints, with the option to create an array
    numpy.random.normal(mu, sigma, {SIZE})
        Normal distribution of random numbers

Numpy also has matrices, which are not the same as arrays
Methods:
    numpy.matrix({ARRAY}, [OPT]dtype={TYPE})
        Changes an array into a matrix
    numpy.asarray({MATRIX})
        Changes a matrix into an array

Finally, numpy has statistics-based methods
Methods:
    {ARRAY}.min()
    {ARRAY}.max()
    {ARRAY}.mean()
    {ARRAY}.median()
    {ARRAY}.std()
        {INT} 
        {FLOAT}
        Standard statistics methods
    numpy.amin(a, axis=b)
    numpy.amax(a, axis=b)
        {ARRAY} -> {INT} -> {ARRAY}
        returns the column or row with the array min or max based on axis=0 or axis=1

Miscellaneous
Methods:
    numpy.arrange(a, b, c)
        {INT} -> {INT} -> {INT} -> {INT ARRAY}
        returns an array of numbers between a and b, with intervals of c
    numpy.linspace(a, b, num=c, [OPT]endpoint = d)
        {FLOAT} -> {FLOAT} -> {INT} -> {BOOL} -> {FLOAT ARRAY}
        returns an array of numbers between a and b, with c number of linear intervals
        to include the last number, consult d
        linspace -> linearly spaced
    numpy.logspace(a, b, num=c, [OPT]endpoint = d)
        {FLOAT} -> {FLOAT} -> {INT} -> {BOOL} -> {FLOAT ARRAY}
        returns an array of numbers between a and b, with c number of logarithmic intervals
        to include the last number, consult d
        logspace -> logarithmically spaced


'''

import statistics
import numpy as np
print ('numpy', np.__version__)
#print(dir(np)) #Prints the methods of numpy

numpyExample = [0,1,-1,0,0]
numpyExample2 = [[1,2],[3,4]]

numpy_array_from_list = np.array(numpyExample)
numpy_bool = np.array(numpyExample, dtype = bool)
numpy_array_from_list2 = np.array(numpyExample2)
numpyList = numpy_array_from_list2.tolist()

print(numpyExample)
print(numpy_array_from_list)

#Day 25 - Pandas


#Day 26 - Python Web


#Day 27 - Python with MongoDB


#Day 28 - API


#Day 29 - Building API


#Day 30 - Conclusions

