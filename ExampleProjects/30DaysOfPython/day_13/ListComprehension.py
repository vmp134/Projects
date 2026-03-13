#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative = [i for i in numbers if i<=0]

#2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
Flatten = [i for nest in list_of_lists for lst in nest for i in lst]
print(Flatten)

#3
TupleList = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]

#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
FlattenCountries = [[strA.upper(), strA[0:3].upper(), strB.upper()] for lst in countries for (strA, strB) in lst]
print(FlattenCountries)

#5
DictCountries = [{'country':strA.upper(), 'city':strB.upper()} for lst in countries for (strA, strB) in lst]
print(DictCountries)

#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
ConcatNames = [strA + " " + strB for lst in names for (strA, strB) in lst]
print(ConcatNames)

#7
slope = lambda y2, y1, x2, x1: (y2-y1)/(x2-x1)