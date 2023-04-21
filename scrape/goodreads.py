import requests
from bs4 import BeautifulSoup
import configparser

# Config
config = configparser.ConfigParser()
config.read('config.ini')
gr_username = config.get('gr', 'username')

import requests
from bs4 import BeautifulSoup

url = f'https://www.goodreads.com/review/list/{gr_username}?shelf=read'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

reviews = soup.find_all('tr', class_='bookalike review')
res = []

for review in reviews:
    title = review.find('td', class_='field title').findChildren()[2].text.strip()
    author = review.find('td', class_='field author').findChildren()[2].text.strip()
    avg_rating = review.find('td', class_='field avg_rating').findChildren()[1].text.strip() 
    date_added = review.find('td', class_='field date_added').findChildren()[1].text.strip() 

    res.append([title, author, avg_rating, date_added])

print(len(res))
