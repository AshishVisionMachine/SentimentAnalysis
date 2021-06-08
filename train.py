from Preprocessing import preprocessing 
from utility import utility
import os
from utility import utility
import pandas as pd
from model import Sentimentmodel
from sklearn.model_selection import train_test_split
import numpy as np

folder_path="tokens"
class_folder=[]
batchsize=8
epoch=2
vsplit=0.2
verbose=0.2


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
    
    
    #print("input is {}".format(label))
    X_train, X_test, y_train, y_test = train_test_split(input, label, test_size=0.33, random_state=42)
    Sentimentmodel_o=Sentimentmodel()
    #model=Sentimentmodel_o.model_train(input,label)
    #model=Sentimentmodel_o.model_compile(model)
    preprocessing_obj= preprocessing()
    #row,=X_train.shape
    #X_train=np.reshape(X_train,(row,1))
    print("value of xtrain is {}".format(X_train))
    
    X_train=preprocessing_obj.stopwordemoval(X_train)
    X_train=preprocessing_obj.lowercasing(X_train)
    #X_train=preprocessing_obj.tokenization(X_train)
    print("value of xtrain after tokenization is {}".format(X_train))

    #X_train=np.reshape(X_train,(1,1,1,914))
    #model=Sentimentmodel_o.model_fit(model,X_train,y_train,batchsize,epoch,vsplit)
    #model=Sentimentmodel_o.model_predict(model,X_test,y_test,verbose)
    
    
    







if __name__ == "__main__":
    train()
    