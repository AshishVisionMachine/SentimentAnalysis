import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class preprocessing:

    def __init__(self,input):
        self.imput=input
        nltk.download('all')

        
        
    def lowercasing(self,input):
        lower_string=input.lower()        
        return lower_string
        
    def tokenization(self,input):
        token_string=word_tokenize(input)
        
        return token_string
        
    def stopwordemoval(self,input):
        stop_words=set(stopwords.words('english'))
        
        return stop_words
        
    def stemming(self,input):
        ps = PorterStemmer()
        stem_word=ps.stem(input)
        return stem_word
        
    def lemmatization(self,input):
        
        return lemmatization_string