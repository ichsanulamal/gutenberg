import re
from os.path import join
from os import makedirs
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from bs4 import BeautifulSoup

# download html and return parsed doc or None on error
def download_url(urlpath):
    try:
        # open a connection to the server
        with urlopen(urlpath, timeout=3) as connection:
            # read the contents of the html doc
            return connection.read()
    except:
        # bad url, socket timeout, http forbidden, etc.
        return None

# decode downloaded html and extract all <a href=""> links
def get_urls_from_html(content):
    # decode the provided content as ascii text
    html = content.decode('utf-8')
    # parse the document as best we can
    soup = BeautifulSoup(html, 'html.parser')
    # find all all of the <a href=""> tags in the document
    atags = soup.find_all('a')
    # get all links from a tags

    res = []
    for tag in atags:
        if tag.get('href') is not None and "#" not in tag.get('href'):
            regexp = re.compile(r'htm')
            if regexp.search(tag.get('href')):
                res.append(tag.get('href'))
    return res

def get_ebook_id(url="https://www.gutenberg.org/files/58025"):
    return url.split("/")[4]

# download one book from project gutenberg
def download_book(ebook_id, save_path):
    # construct the download url
    url = f'https://www.gutenberg.org/cache/epub/{ebook_id}/pg{ebook_id}.txt'
    # download the content
    print(url)
    data = download_url(url)
    if data is None:
        return f'Failed to download {url}'
    # create local path
    save_file = join(save_path, f'{ebook_id}.txt')
    # save book to file
    with open(save_file, 'wb') as file:
        file.write(data)
    return f'Saved {save_file}'

# download all top books from project gutenberg
def download_all_books(url, save_path):
    # download the page that lists top books
    data = download_url(url)
    print(f'.downloaded {url}')
    # extract all links from the page
    links = get_urls_from_html(data)
    [ download_book(get_ebook_id(url), save_path) for url in links ]

# entry point
URL = 'https://www.gutenberg.org/files/58025/58025-h/58025-h.htm#N51548'
DIR = 'books'
# download top books
download_all_books(URL, DIR)