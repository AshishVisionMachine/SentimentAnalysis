import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class preprocessing:

    def __init__(self,input):
        self.input=input
        
    def lowercasing(self,input):
        lower_string=input.lower()
        
        retrun lower_string
        
    def tokenization(self,input):
        token_string=word_tokenize(input)
        
        retrun token_string
        
    def stopwordemoval(self,input):
        stop_words=set(stopwords.words('english'))
        
        retrun stop_words
        
    def stemming(self,input):
        ps = PorterStemmer()
        stem_word=ps.stem(input)
        retrun stem_word
        
    def lemmatization(self,input):
        
        retrun lemmatization_string