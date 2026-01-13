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
 

#3
url3 = 'https://restcountries.eu/rest/v2/all'
countries = requests.get(url3).json()

#4
import BeautifulSoup4