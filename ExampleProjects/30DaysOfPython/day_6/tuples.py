#1
Empty = tuple()

#2
Brothers = ("John", "Josiah", "Arthur", "Charles")
Sisters = ("Sadie", "Tilly", "Mary-Beth")

#3
Siblings = Brothers + Sisters

#4
print(len(Siblings))

#5
Family = Siblings + ("Dutch", "Hosea")

#1
a, b, c, d, e, f, g, h, i = Family

#2
Fruits = ("Apple, Pear")
Vegetables = ("Broccoli", "Cabbage")
AnimalProducts = ("Eggs", "Dairy")
Foodstuffs = Fruits + Vegetables + AnimalProducts

#3
About = list(Foodstuffs)

#4
Item = Foodstuffs[len(Foodstuffs)/2]

#5
FirstThree = Foodstuffs[0:2]
LastTree = Foodstuffs[-2:]

#6
del Foodstuffs

#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
BoolA = "Estonia" in nordic_countries
BoolB = "Iceland" in nordic_countries
