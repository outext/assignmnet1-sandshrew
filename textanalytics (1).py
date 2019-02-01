'''This assignmnet we try to hands on to understand basics of Natural Language Processing'''

import requests
from bs4 import BeautifulSoup
import nltk
from nltk import word_tokenize
from nltk.corpus  import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

#After installing nltk you need to download a required packages like stopwords etc, inorder to do so you need to go python3 console and then type 'nltk.download(package name)
#import stopwords similar to word_tokenize that was given in word_tokenize.py. Also remove the '(' and ')'.

def download(g):
    """ This function downloads the html data from the url 
        and finds all of the <blockquote> tags."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    tags = soup.find_all("blockquote")
    
    return tags

def tokenize(tags):
    """ This function downloads gives you tokenized words ."""
    tokens = []
    for tag in tags:
        for s in tag.strings:
            tokens.extend(word_tokenize(s))
    return tokens


def stopw(b):
    """ This function should remove the stopwords from the input given to function"""
    # TODO add code here
    # remove the, a, and
    return[]


def stemm(c):
    """ This function will group similar type of words"""
    # TODO add code here
    return[]



def lemmatize(d):
    "The function will group similar type of words"
    # TODO add code here
    return[]

def frequency(e):
    """ This function must show the frequecy of each word for the given input """
    #TODO add code here
    return[]

def show2(f):
   """This function will show two words with highest frequency"""
   # TODO add code here
   return[]

if __name__ == '__main__':
    url = "http://catdir.loc.gov/catdir/enhancements/fy0665/2006042906-s.html"
    text = (download(url))
    #print(text)
    tokenized_text = tokenize(text)
    print(tokenized_text)
    """
    sw = stopw(tokenized_text)
    print(sw)
    stemz = stemm(sw)
    print(stemz)
    lem = lemmatize(stemz)
    print(lem)
    freq = frequency(lem)
    print(freq)
    top2 = show2(freq)
    print(top2)
    """

#Download the package as per requirements using nltk.download(). We tend to download only the packages that we require since since its nltk repository is more than 2 GB.

#Nexr word_tokenize.py








