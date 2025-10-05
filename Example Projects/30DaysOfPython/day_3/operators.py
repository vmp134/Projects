Age = 19
Height = 178
Comp = 2j + 49

def TriangleArea(a,b): 
    return a*b/2

def TrianglePerimeter(a,b,c):
    return a+b+c

def RectangleStuff(a,b):
    area = a*b
    perim = (2*a) + (2*b)

def CircleStuff(a):
    area = 3.14 * a**2
    circum = 3.14*a*2

EquationA = 2j - 2
Yintercept = EquationA(0)
Xintercept = EquationA(2)
SlopeA = EquationA(1) - EquationA(0)

SlopeB = (10 - 2) / (6 - 2)

if (SlopeB > SlopeA):
    True

x = -3
EquationB = x**2 + 6*x + 9

if (len('python') > len('dragon')): True

if ('on' in 'python' and 'dragon'): True

if ('jargon' in 'I hope this course is not full of jargon'): True

if ('on' in 'python' and 'dragon'): False

str(float(len('python')))

def isEven(a):
    a%2 == 0

if (int(2.7) == 7//3): True

if ('10' == type(10)): True

if (int('9.8') == 10): True

#Hours
print('Enter hours:')
hours = int(input)
print('Enter rate per hour:')
rate = int(input)
print('Your weekly earning is ' + rate*hours)

#Years
print('Enter number of years you have lived: ')
years = int(input)
print('You have lived for ' + years*365*24*60*60 + ' seconds.')

#Table
for i in range (4):
    print((1+i) + ' ' + 1 + ' ' + (1+i) + ' ' + ((1+i)**2) + ' ' + ((1+i)**3))
