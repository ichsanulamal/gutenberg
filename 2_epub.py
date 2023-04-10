import ebooklib
from ebooklib import epub
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

book = epub.read_epub('books/1998.epub')

text = ''
for item in book.get_items():
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
        text += item.get_content().decode('utf-8')

# Clean the text
# Remove HTML tags
text = re.sub('<[^<]+?>', '', text)

# Tokenize the text
tokens = nltk.word_tokenize(text)

# Remove punctuation and convert to lowercase
tokens = [token.lower() for token in tokens if token.isalpha()]

# Remove stopwords
stop_words = set(stopwords.words('english'))
tokens = [token for token in tokens if not token in stop_words]

# Lemmatize the tokens
lemmatizer = WordNetLemmatizer()
tokens = [lemmatizer.lemmatize(token) for token in tokens]

# Convert the list of tokens back to text
clean_text = ' '.join(tokens)

# # print(book.title, book.language)        
