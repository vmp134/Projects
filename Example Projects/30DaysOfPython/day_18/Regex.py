import re

#1
paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."

def mostFrequentWord(words): 
    noPunct = re.sub(r"[^\w\s]", "", words)
    wordArray = re.split(" ", noPunct)
    ret = dict()
    for word in wordArray:
        if ret.get(word) == None: ret[word] = 1
        else: ret[word] += 1
    wordSort = sorted(ret.items(), key=lambda count: count[1], reverse=True)
    return wordSort[0]

print(mostFrequentWord(paragraph))

#2
text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles."

def extractDistancefromPoints(words):
    noWords = re.findall(r"-?\d+", words)
    intArray = [int(i) for i in noWords]
    sortedPoints = sorted(intArray)
    return abs(sortedPoints[0] - sortedPoints[len(sortedPoints)-1])

print(extractDistancefromPoints(text))

#1

def isValidVariable(word):
    if word == "": return False

    first = re.match(r"^[A-Za-z_]", word)
    see = re.match(r"^[A-Za-z0-9_]+$", word)
    if first != None and see != None: return True
    else: return False

print(isValidVariable("first_name"))
print(isValidVariable("first-name"))
print(isValidVariable("1first_name"))
print(isValidVariable("firstname"))

#1
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def cleanText(text):
    return re.sub(r"[!@#$%^&*(),.?;:]", "", text)

print(cleanText(sentence))

#I'm not doing the most frequent words I pretty much already did that