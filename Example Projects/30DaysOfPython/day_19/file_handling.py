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



#5



#6



#7



#8



#9


