import requests
from bs4 import BeautifulSoup

url = 'https://myanimelist.net/animelist/laataiasu?status=7'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

items = soup.find_all('tbody', class_='list-item')
for item in items:
    table_data = item.findChild()

    
    title = table_data.find('td', class_="data title clearfix").findChild()
    score = table_data.find_all(class_="data score")
    type = table_data.find(class_="data type")
    progress = table_data.find('a', class_="link sort").text.strip() 
    print(print(title))


