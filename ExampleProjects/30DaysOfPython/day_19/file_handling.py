#1
def countLinesWords(file):
    f = open(file, "r")
    fileString = f.read()
    words = len(fileString.split())
    lines = len(fileString.splitlines())
    f.close()
    return (lines ,words)

#2
import json
def mostSpokenLanguages(file, num):
    f = open(file, "r")
    countriesDict = json.load(f)
    languages = {}
    for country in countriesDict:
        for language in country['languages']:
            if language in languages:
                languages[language] += 1
            else:
                languages[language] = 1
    f.close()
    return (sorted(languages.items(), key=lambda language: language[1]))[-num:]
print(mostSpokenLanguages("Projects/Example Projects/30DaysOfPython/Misc/data/countries_data.json", 10))

#3
def mostPopulated(file, num):
    with open(file, "r") as f:
        countriesDict = json.load(f)
        populationSort = sorted(countriesDict, key=lambda country: country['population'])
        return populationSort[-num:]

#4
def listOfAddresses(file):
    with open(file, "r") as f:
        arr = f.readlines()
        ret = list()
        for item in arr: 
            if "Author" in item: ret.append(item[8:-1])
        return ret
print(listOfAddresses("Projects/Example Projects/30DaysOfPython/Misc/data/email_exchanges_big.txt"))

#5
def MostCommonWords(file, num):
    with open(file, "r") as f:
        arr = f.read().split()
        ret = dict()
        for word in arr:
            if word in ret: ret[word] += 1
            else: ret[word] = 1
        return sorted(ret.items(), key=lambda word: word[1])[-num:]


#6
#function application

#7
#Seems like a fully-fledged project for another time

#8
#Function application

#9
def CountingProg(file):
    with open(file, "r") as f:
        arr = f.readlines()
        ret = {"python":0, "javascript":0, "java":0}
        for line in arr:
            if "python" in line.lower(): ret["python"] += 1
            elif "javascript" in line.lower(): ret["javascript"] += 1
            elif "java" in line.lower(): ret["java"] += 1
        return sorted(ret.items(), key=lambda language: language[1])

