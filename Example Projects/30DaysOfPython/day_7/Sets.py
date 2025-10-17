# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1
length = len(it_companies)

#2
it_companies.add("Twitter")

#3
it_companies.update({"Meta", "Palantir"})

#4
it_companies.remove("Google")

#5
'''
Remove deletes the element from the set, but returns an error if not found
Discard does not raise errors.
'''

#1
C = A + B

#2
Inter = A.intersection(B)

#3
IsSub = A.issubset(B)

#4
Disjoint = (A.intersection(B) == set())

#5
C = A + B
D = B + A

#6
SymDif = A.symmetric_difference(B)

#7
del A
del B

#1
AgeSet = set(age)
print(len(age) > len(AgeSet))

#2
'''
String is an ordered combination of characters
List is an ordered combination of items marked by indices
Tuple is an immutable, ordered combination of items marked by indices
Set is an unordered combination of items
'''

#3
WordSet = set(("I am a teacher and I love to inspire and teach people").split(" "))
