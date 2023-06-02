import requests
from bs4 import BeautifulSoup
from time import sleep
import random
import csv

url = 'https://daraba.art/ge/artworks'
payloads = {'page': 1}

file = open('art.csv', 'w', newline='\n', encoding='UTF-8_sig')
csv_obj = csv.writer(file)
csv_obj.writerow(['სათაური', 'ავტორი', 'ფასი'])
while payloads['page'] <= 5:
    response = requests.get(url, params = payloads)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    art_soup = soup.find('div', class_ = 'article-container')
    all_art = art_soup.find_all('div', class_ = 'article-item')
    for art in all_art:
        title = art.h4.a.text.strip()
        author = art.h6.a.text.strip()
        price = art.find('span', class_ = 'new-price').text
        print(title, author, price)
        csv_obj.writerow([title, author, price])

    payloads['page'] += 1
    sleep(random.randint(15,20))
