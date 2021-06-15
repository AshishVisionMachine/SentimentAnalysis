from nltk.corpus import movie_reviews
from Preprocessing import preprocessing 
from utility import utility
import os
from utility import utility
import pandas as pd
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
 
 
def word_feats(words):
    return dict([(word, True) for word in words])
 


def main():
    negids = movie_reviews.fileids('neg')
    posids = movie_reviews.fileids('pos')
 
    negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
    posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]
 
    negcutoff = len(negfeats)*3/4
    poscutoff = len(posfeats)*3/4
 
    trainfeats = negfeats[:int(negcutoff)] + posfeats[:int(poscutoff)]
    testfeats = negfeats[int(negcutoff):] + posfeats[int(poscutoff):]
    print('train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats)))
    
    print("train feature are {}".format(trainfeats))
 
    classifier = NaiveBayesClassifier.train(trainfeats)
    print('accuracy:', nltk.classify.util.accuracy(classifier, testfeats))
    classifier.show_most_informative_features()

 





if __name__ == "__main__":
    main()