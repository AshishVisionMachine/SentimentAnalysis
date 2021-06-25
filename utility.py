import os
import csv
import pandas as pd


class utility:
    def __init__(self,init="default"):
        self.init=init
        
    def get_path(self,folder_name):
    
        dir_path=os.path.abspath(folder_name)
        
        return dir_path
    
    
    def get_file_list(self,dir_path):
        file_list=os.listdir(dir_path)
        
        return file_list
    
    def file_open(self,filename):
        print("open file name is {} \n".format(filename))

        file_f = open(filename, encoding="utf8")
        
        return file_f
        
        
    def read_file(self,filehandle):
        data=filehandle.read()
        return data
    
    def read_line(self,filehandle,line):
        line_Data=filehandle.readlines(-1)
        return line_Data
    
    #def file_write(self,file_name):
    
    def write_csv_file(self,data,label):
        
        with open('email_.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Data", "Label"])
            for j in range(len(label)):
                for i in range(len(data)):
                    writer.writerow([data[i],label[j]])
    
    def read_csv(self):
        data=[]
        label=[]
        input_val = pd.read_csv("Sentiment.csv",usecols=['Data','Label'])
        data=input_val["Data"]
        label=input_val['Label']
        return data,label
