import requests
from bs4 import BeautifulSoup
import configparser

# Config
config = configparser.ConfigParser()
config.read('config.ini')
mdl_username = config.get('mdl', 'username')

# Main app
url = 'https://mydramalist.com/dramalist/' + mdl_username
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

items = soup.find_all('tr')

res = []
for item in items:
    try:
        title = item.findChildren()[1].findChildren()[2].text.strip()
        country = item.findChildren()[6].text.strip()
        year = item.findChildren()[7].text.strip()
        type = item.findChildren()[8].text.strip()
        score = item.findChildren()[12].text.strip()
        progress = item.findChildren()[13].text.strip()
    except:
        pass
    res.append([title, country, year, type, score, progress])


print(res)
