import string
import math
import numpy as np
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')

from collections import Counter

def read_book(title_path): 
    """Read a book and return it as a string""" 
    with open(title_path,"r",encoding = "utf8") as current_file:            
        return current_file.read() 

def pre_processing(document, is_stopwords=True):
    document = document.replace("\n","").replace("\r","") 
    document = document.lower()
    document = document.translate(str.maketrans('', '', string.punctuation+'“'+'”'))

    # TODO: remove stopwords
    stop_words = set(stopwords.words('english')) 
    word_tokens = word_tokenize(document)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    document_clean = ' '.join(filtered_sentence)
    return document_clean

def tf_idf(document):
    # split the document into words
    words = document.split()

    # calculate term frequency and document frequency
    tf = Counter(words)
    df = Counter(set(words))

    # calculate inverse document frequency
    num_docs = 1  # assuming only one document in the input file
    idf = {word: math.log(num_docs / count) for word, count in df.items()}

    # calculate tf-idf weight
    tfidf = {word: freq * idf[word] for word, freq in tf.items()}

    # create a list of tuples with the data
    data = [(i+1, word, freq, freq/len(words)*100, df[word], idf[word], tfidf[word])
            for i, (word, freq) in enumerate(tf.most_common())]

    # create a pandas DataFrame from the data
    df = pd.DataFrame(data, columns=['Rank', 'Word', 'Term Frequency', 'TF Percentage',
                                    'Document Frequency', 'Inverse Document Frequency', 'TFIDF Weight'])

    return df

def generate_N_grams(document, ngram=1):
    words=[word for word in document.split(" ")]  
    temp=zip(*[words[i:] for i in range(0,ngram)])
    ans=[' '.join(ngram) for ngram in temp]
    return ans

document = read_book(r"C:\Users\ichsan\Documents\proj\gitenberg\books\51710.txt") 
document = pre_processing(document)

# start of plot
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                min_font_size = 10).generate(document)
 
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
 
plt.show()
# end of plot

document = tf_idf(document)






