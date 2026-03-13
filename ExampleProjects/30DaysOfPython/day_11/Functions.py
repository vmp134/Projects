#1
def add_two_numers(a, b):
    return a+b

#2
def circle_area(r):
    return 3.14*(r**2)

#3
def add_all_nums(*nums):
    ret = 0
    for num in nums:
        ret += num
    return ret

#4
def convertCtoF(C):
    return ((C*9)/5)+32

#5
def checkSeason(string):
    if (string.lower() == 'december' or 'january' or 'february'):
        return "Winter"
    elif (string.lower() == 'march' or 'april' or 'may'):
        return 'Spring'
    elif (string.lower() == 'june' or 'july' or 'august'):
        return 'Summer'
    elif (string.lower() == 'September' or 'October' or 'November'):
        return 'Autumn'
    else:
        return "Error: Not a month!"

#6
def calculateSlope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)

#7
def solve_quadratic_eqn(a,b,c):
    upper = (-b + ((b*b)-(4*a*c))**0.5)/(2*a)
    lower = (-b - ((b*b)-(4*a*c))**0.5)/(2*a)
    return (upper, lower)

#8
def print_list(lst):
    for string in lst:
        print(string, sep = " ")

#9
def reverse_list(lst):
    i, j = 0, len(lst)-1
    while (i < j):
        temp = lst[j]
        lst[j] = lst[i]
        lst[i] = temp
        i += 1
        j -= 1

#10
def CapitalizeListItems(lst):
    for i in range(len(lst)):
        lst[i] = lst[i].upper()

#11
def add_item(lst, a):
    lst.append(a)

#12
def remove_item(lst, a):
    lst.remove(a)

#13
def sum_of_nums(a):
    total = 0
    for i in range(a):
        total += i
    return total

#14
def sum_of_odds(a):
    total = 0
    for i in range(a):
        if (i%2 == 0):
            total += i
    return total

#15
def sum_of_evens(a):
    total = 0
    for i in range(a):
        if (i%2 != 0):
            total += i
    return total

#1
def evens_and_odds(a):
    evens, odds = 0,0
    for i in range(a+1):
        if (i%2 == 0):
            evens += 1
        else:
            odds += 1
    return (evens, odds)

#2
def factorial(a):
    ret = 1
    for i in range (a+1):
        ret *= i
    return ret

#3
def is_empty(lst):
    if len(lst) == 0:
        return True
    return False

#4
'''NOT DOING ALL THAT'''

#1
'''NOT DOING THIS EITHER >:('''

#2
'''O(N^2) makes me sad'''
def uniqueList(lst):
    for i in range(len(lst)):
        temp = lst.pop(i)
        if temp in list: return False
    return True

#3
def sameType(lst):
    typePrev = type(lst[0])
    for i in range(1, len(lst)):
        if type(lst[i]) != typePrev:
            return False
        typePrev = type(lst[i])
    return True

#4
def ValidVariable(string):
    if string[0] == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or '0':
        return False
    elif '!' or '@' or '#' or '$' or '%' or '^' or '&' or '*' or '(' or ')' or '-' or '+' or '=' in string:
        return False
    return True

#5
'''We did this last time'''