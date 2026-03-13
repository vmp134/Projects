#1
String1 = "Thirty " + "Days " + "Of " + "Python"

#2
String2 = "Coding " + "For " + "All"

#3
Company = "Coding For All"

#4
print(Company)

#5
print(len(Company))

#6
Upper = Company.upper()

#7
Lower = Company.lower()

#8
Caps = Company.capitalize()
Title = Company.title() 
SwapCase = Company.swapcase()

#9
Slice = Company[0:5]

#10
Check = Company.index("Coding")

#11
Replaced1 = Company.replace("Coding", "Python") 

#12
Replaced2 = ("Python For Everyone").replace("Everyone", "All")

#13
ArrayString = Company.split(" ")

#14
ArrayCompanies = ("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon").split(", ")

#15
CharacterAt = Company[0]

#16
LastIndex = Company.len() - 1

#17
IndexTen = Company[10]

#18
Acronym1 = ("Python For Everyone")[0:7:11]

#19
Acronym2 = Company[0:7:11]

#20
IndexOfC = Company.index("c")

#21
IndexOfF = Company.index("f")

#22
LastL = ("Coding For All People").rfind("l")

#23
IndexOfBecause = ('You cannot end a sentence with because because because is a conjunction').index("because")

#24
LastOfBecause = ('You cannot end a sentence with because because because is a conjunction').rindex("because")

#25
SliceBecause = ('You cannot end a sentence with because because because is a conjunction')[31:53]

#26
IndexOfBecause = ('You cannot end a sentence with because because because is a conjunction').index("because")

#27
SliceBecause = ('You cannot end a sentence with because because because is a conjunction')[31:53]

#28
StartCoding = Company.startswith("coding")

#29
EndCoding = Company.endswith("coding")

#30
Stripped = ('   Coding For All      ').strip(" ")

#31 - thirty_days_of_python - identifiers can't start with numbers.

#32
Joined = (" ").join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'])

#33
Escape = "I am enjoying this challenge.\nI just wonder what is next."

#34
Tab = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"

#35
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area)
print(formated_string)

#36
a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))