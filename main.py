import requests
from bs4 import BeautifulSoup
import re

URL = 'https://studynow.ru/dicta/allwords'
page = requests.get(URL)


soup = BeautifulSoup(page.content, 'html.parser')
lis = []
r = soup.find_all(id='wordlist')
for r in r:
    result = r.find_all('td')
list_of_raw_data = re.findall('<td>(.*?)</td>',str(result))

eng_words = []
rus_words = []

flag = 0
for word in list_of_raw_data:
    if flag % 3 == 1:
        eng_words.append(word)
    if flag % 3 == 2:
        rus_words.append(word)
    flag += 1
    if flag == 301:
        break
flag = 1
for x in eng_words:
    print(flag,x)
    flag += 1
for x in rus_words:
    print(x)


