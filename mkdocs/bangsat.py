import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

# Set the URL of the website page you want to translate
url = "https://www.gutenberg.org/files/52190/52190-h/52190-h.htm"

# Get the HTML content of the website page
response = requests.get(url)
html_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the text elements in the HTML content and translate them
for text_elem in soup.find_all(text=True):
    # Split the text into chunks of 5000 characters or less
    chunks = [text_elem[i:i+5000] for i in range(0, len(text_elem), 5000)]
    # Translate each chunk and replace the original text with the translated text
    for i, chunk in enumerate(chunks):
        try:
            translated = GoogleTranslator(source='en', target='id').translate(chunk) 
            text_elem.replace_with(translated if i == 0 else f"{text_elem}{translated}")
        except:
            pass

# Export the translated HTML content to a file
with open('translated.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
