from Preprocessing import preprocessing 
from utility import utility
import os
from utility import utility
import pandas as pd
from model import Sentimentmodel
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder

folder_path="tokens"
class_folder=[]
batchsize=8
epoch=2
vsplit=0.2
verbose=0.2
preprocessing_obj= preprocessing()
ytrain=[1,2,3,4,5,1,2,0,2,2]

def pre_process(input):
    #X_t=preprocessing_obj.tokenization(input)
    #X_train=preprocessing_obj.stopwordemoval(input)
    #X_t=preprocessing_obj.lowercasing(X_train)
    #print("X_train is {}".format(X_t))

    pre_process_val=preprocessing_obj.bagofwords(input)
    print("Bag of words for this {}".format(len(pre_process_val)))
    f = open("bagofword.txt", "a")
    f.write((str(pre_process_val[:100])))
    f.close()

    return pre_process_val

def load_data():
    utli_obj=utility()
    print(utli_obj.get_path(folder_path))
    
    path=utli_obj.get_path(folder_path)
    
    class_folder=utli_obj.get_file_list(path)
    print("folder is {} and {}".format(class_folder[0],class_folder[1]))
    data,label=utli_obj.read_csv()
    
    count=0
    return data,label
    
def train():
    print ("training start ")
    
    input,label=load_data()
    
    
    print("label is {}".format(label))
    X_train, X_test, y_train, y_test = train_test_split(input, label, test_size=0.10, random_state=42)
    raw_train_ds=X_train,y_train
    raw_val_ds=X_test,y_test
    Sentimentmodel_o=Sentimentmodel()
    #model=Sentimentmodel_o.model_train(input,label)
    #model=Sentimentmodel_o.model_compile(model)
    row,=X_train.shape
    print("shape of X_TAIN IS {}".format(X_train.shape))
    #X_train=np.reshape(X_train,(row,1))
    
    row,=X_test.shape
    #X_test=np.reshape(X_test,(row,1))
    
    print("value of y_test is {}".format(y_test.shape))
    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    from sklearn.compose import ColumnTransformer
#Encode Country Column
    #labelencoder_X = LabelEncoder()
    #X_train = labelencoder_X.fit_transform(X_train)
   
    onehotencoder = OneHotEncoder(handle_unknown='ignore')
    X_train = onehotencoder.fit_transform(X_train).toarray()
    
    onehotencoder = OneHotEncoder(handle_unknown='ignore')
    X_test = onehotencoder.fit_transform(X_test).toarray()
    
    #X_train=pre_process(X_train)
    #print("X_train is {}".format(X_train))
    #X_test=pre_process(X_test)
    #y_train=preprocessing_obj.tfidf(y_train)
    #y_test=preprocessing_obj.tfidf(y_test)
    y_train=[0 if x=="neg" else x for x in y_train]
    y_train=[1 if x=="pos" else x for x in y_train]
    
    y_test=[0 if x=="neg" else x for x in y_test]
    y_test=[1 if x=="pos" else x for x in y_test]

    print("SHAPE of X_TRAIN {} X_TEST  {}  Y_TRAIN  {}   Y_TEST {} ".format(X_train.shape,X_test.shape,np.shape(y_train),np.shape(y_test)))

    
    #print("y_train IS {}".format(y_train))
    
    
    
   # print("value of xtrain after tokenization is {}".format(X_train))
    
    model=Sentimentmodel_o.model_train()
    model.summary()

    model=Sentimentmodel_o.model_compile(model)
    history=Sentimentmodel_o.model_fit(model,X_train,y_train,X_test,y_test)

    #X_train=np.reshape(X_train,(1,1,1,914))
    #model=Sentimentmodel_o.model_fit(model,X_train,y_train,batchsize,epoch,vsplit)
    test_ds={"Hi we are doing good","not happy with outcome of discussion"}
    test_ds=pre_process(test_ds)

    #result=Sentimentmodel_o.model_predict(model,test_ds)
    
    #print("major prediction rsult is {}".format(result))
    
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()
    







if __name__ == "__main__":
    train()
    