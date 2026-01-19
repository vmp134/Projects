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
    pip install [name]
    pip uninstall [name]
    pip list
        see the installed packages on the machine
    pip show [name]
        see the info about a package
        --verbose adds more details
    pip freeze 
        installed packages with versions

To get read data from a website or API, we can use a package called requests
Methods:
    .get()        
        opens network and fetches data from url, returns {RESPONSE} Object
    .status_code
        returns status of object, success, failure, etc.
    .headers
        checks header types
    .text
        extracts text from {RESPONSE}
    .json
        extracts json from {RESPONSE} 

Methods Example
'''

import requests
url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'
response = requests.get(url)
print(response)
print(response.status_code)
print(response.headers) 
print(response.text)

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
'''

import requests
from bs4 import BeautifulSoup

url2 = 'https://archive.ics.uci.edu/dataset/320/student+performance'
response = requests.get(url)
status = response.status_code
print(status)

#Day 23 - Virtual Environment


#Day 24 - Statistics


#Day 25 - Pandas


#Day 26 - Python Web


#Day 27 - Python with MongoDB


#Day 28 - API


#Day 29 - Building API


#Day 30 - Conclusions

