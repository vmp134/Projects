#1
print("Enter your age: ")
age = str(input())
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print("You need " + 18-age + " more years to learn to drive.")

#2
print("Enter your age: ")
age = str(input())
if age == 19:
    print("You are the same age as me.")
elif age == 18 or age == 20:
    if age == 18: print("You are one year younger than me.")
    else: print("You are one year older than me.")
elif age < 18: print ("You are " + 19-age + " years younger than me.")
else: print ("You are " + age-19 + " years older than me.")

#3
print("Enter number one: ")
numA = int(input())
print("Enter number two: ")
numB = int(input())
if numA > numB:
    print(numA + " is greater than " + numB)
elif numB > numA:
    print(numA + " is less than " + numB)
else: 
    print(numA + " is equal to " + numB)

#1
score = int(input)
grade = str
if score >= 80: grade = "A"
elif score >= 70: grade = "B"
elif score >= 60: grade = "C"
elif score >= 50: grade = "D"
else: grade = "F"

#2
month = str(input()).lower()
season = str
if month == "december" or "january" or "february": season = "Winter"
elif month == "march" or "april" or "may": season = "Spring"
elif month == "june" or "july" or "august": season = "Summer"
elif month == "september" or "october" or "november": season = "Autumn"
else: print("Misspelled Month")

#3
fruit = str(input).lower()
fruits = ['banana', 'orange', 'mango', 'lemon']
if fruit in fruits: print('That fruit already exist in the list')
else: fruits.append(fruit)

#1
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
        }
    }

if person.get("skills") != None: print(person.get("skills")[len(person.get("skills")/2)])
if person.get("skills") != None: 
    if "Python" in person.get("skills"): print("True")
    else: print("False")
    if (("Javascript" and "React") in person.get("skills")) and len(person.get("skills")) == 2:
        print('He is a front end developer')
    elif (("Node" and "Python" and "MongoDB") in person.get("skills")) and len(person.get("skills")) == 3:
        print('He is a backend developer')
    elif (("Node" and "React" and "MongoDB") in person.get("skills")) and len(person.get("skills")) == 3:
        print('He is a fullstack developer')
    else: print('unknown title')
if person.get("is_married") and person.get("country") == "Finland":
    print(person.get("first_name") + " " + person.get("last_name") + " lives in " + person.get("country") + ". He is married.")