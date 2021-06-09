import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.metrics.pairwise import cosine_similarity


class preprocessing:

    def __init__(self,input="Sentiment"):
        self.input=input
        #nltk.download('all')

        
        
    def lowercasing(self,input):
        list_lower=[]
        for s in input:
            str_l=' '.join(map(str, s))
            list_lower.append(str_l.lower())        
        return list_lower
        
    def tokenization(self,input):
        list_token=[]
        for str in input :
            list_token.append(word_tokenize(str))
        
        return list_token
        
    def stopwordemoval(self,input):
        list_stop=[]
        stop_words=stopwords.words('english')
        for str in input:
           token_word=self.tokenization(str)
           for str_s in token_word:
                if str_s not in stop_words:
                    list_stop.append(str_s)
 
        return list_stop
        
    def stemming(self,input):
        ps = PorterStemmer()
        stem_word=ps.stem(input)
        return stem_word
        
    def lemmatization(self,input):
        
        return lemmatization_string
        
    def tfidf(self,input):
        tfid=TfidfVectorizer(max_df=0.90, min_df=1,max_features=1000,stop_words='english')

        tfid_mat=tfid.fit_transform(input)

        df_tf= pd.DataFrame(tfid_mat.todense())
        
        print("dimention is  {} \n".format(df_tf.shape))
        
        return df_tf
        
    def bagofwords(self,input):
        countvector=CountVectorizer(ngram_vect=(1,1),stop_words='english')

        countvectmat=countvector.fit_transform(input)

        countvectfr= pd.DataFrame(countvectmat.todense())
        
        return countvectfr
        
    def cosinesimilarity(self,vectormatrix,vector1,vector2):
        cosine_matrix = cosine_similarity(vectormatrix)
        return create_dataframe(cosine_matrix,[vector1,vector1])