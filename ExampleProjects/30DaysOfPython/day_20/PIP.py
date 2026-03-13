#1
import requests
url = 'https://www.gutenberg.org/cache/epub/1260/pg1260-images.html'
resp = requests.get(url)
arr = resp.text.split()
common = dict()
for word in arr:
    if word in common: common[word] += 1
    else: common[word] = 1
common = sorted(common.items(), key=lambda word: word[1], reverse = True)

#print(common[:10])

#2
url2 = 'https://api.thecatapi.com/v1/breeds'
cats = requests.get(url2).json()
import statistics

def values(cats, category):
    ret = [100,-1,0,0,0] #Min, Max, Mean, Median, SD
    data = []
    for cat in cats:
        if cat.get(category, -1) == -1: continue
        else: 
            val = (int(cat[category][0]) + int(cat[category][-1]))/2
            if val < ret[0]: ret[0] = val
            if val > ret[1]: ret[1] = val
            data.append(val)
    ret[2] = statistics.mean(data)
    ret[3] = statistics.median(data)
    ret[4] = statistics.stdev(data)
    return ret

print(values(cats, 'life_span'))

def countryCats(cats, category):
    ret = dict()
    for cat in cats:
        country = cat[category]
        if country in ret: ret[country] += 1
        else: ret[country] = 1
    return ret

print(countryCats(cats, 'origin'))

#3
url3 = 'https://restcountries.eu/rest/v2/all'
#countries = requests.get(url3).json()
#same concept, there's just an error getting this

#4
import bs4
url4 = 'https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic'
cancer = requests.get(url4)