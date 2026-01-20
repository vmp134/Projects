import requests
from bs4 import BeautifulSoup

#1
url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
print(response.status_code)
content = response.content
soup = BeautifulSoup(content, "html.parser")
#We will figure out HTML Later

#2
url2 = "https://archive.ics.uci.edu/ml/datasets.php"
response = requests.get(url2)
print(response.status_code)
#This gives a 404 error. Skipping

#3
url3 = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
print(response.status_code)
#Also gives a 404