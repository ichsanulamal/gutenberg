from googletrans import Translator
from bs4 import BeautifulSoup

# Load the HTML file
with open('example.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Extract the text content from the HTML
text = soup.get_text()

# Translate the text to Indonesian
translator = Translator()
translated_text = translator.translate(text, dest='id').text

# Replace the English text with the translated text in the HTML
soup.body.string = translated_text

# Save the translated HTML to a new file
with open('example_id.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
