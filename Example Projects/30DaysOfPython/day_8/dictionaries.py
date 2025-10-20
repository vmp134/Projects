#1
dog = {}

#2
dog["Name"] = "Rex"
dog["Color"] = "White"
dog["Breed"] = "German Shepherd"
dog["Legs"] = 4
dog["Age"] = 6

#3 
student = {"first_name":"Veritas", "last_name":"Ratio", "gender":"male", "age":"40", "marital_status":"single", "skills":[], "country":"Zanzibar", "city":"", "address":""}

#4
print(len(student))

#5
print(student.get("skills") + " " + type(student.get("skills")))

#6
student["skills"].append("Debate", "Speech")

#7
KeyList = student.keys()

#8
ValueList = student.values()

#9
TupleList = student.items()

#10
del student["skills"]

#11
del student
