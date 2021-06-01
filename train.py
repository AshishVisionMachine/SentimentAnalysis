from Preprocessing import preprocessing 
from utility import utility
import os
from utility import utility
import pandas as pd
from model import Sentimentmodel

folder_path="tokens"
class_folder=[]


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
    
    print("input is {}".format(label))
    Sentimentmodel_o=Sentimentmodel()
    Sentimentmodel_o.model_train(input,label)
    
    







if __name__ == "__main__":
    train()
    