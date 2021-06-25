from Preprocessing import preprocessing 
from utility import utility
import os
from utility import utility
import pandas as pd




input_string="I am , feeling Good today"
test_string="Hi"
#folder_path ="tokens"
folder_path="Dataset"
class_folder=[]

def main():
    
    
    utli_obj=utility()
    print(utli_obj.get_path(folder_path))
    
    path=utli_obj.get_path(folder_path)
    
    print(utli_obj.get_file_list(path))
    class_folder=utli_obj.get_file_list(path)
    count=0
    class_count=0
    data=[]
    
    for file in utli_obj.get_file_list(path):
        #print("file name is {} \n".format(file))
        data_fi=utli_obj.file_open(os.path.join(path,file))
        data_file =utli_obj.read_file(data_fi)
        data_line =utli_obj.read_line(data_fi,30)
        print("file data is {} \n".format(data_line))
        for line in data_file :
            #data.append(line)
            #print("file data is {} \n".format(line))
            count +=1
            if count==5:
                break

            
        
    #utli_obj.write_csv_file(data,class_folder) 
        
       
    '''
    for folder in utli_obj.get_file_list(path):
        print("folder name's are {} \n".format(folder))
        #print("list of file is {}".format(utli_obj.get_file_list(os.path.join(path,folder))))
        for file in utli_obj.get_file_list(os.path.join(path,folder)) :
            
            print("print fil ein folder is {}" .format(file))
            #utility=utility()
            file_f=utli_obj.file_open(os.path.join(os.path.join(path,folder),file))
            data.append(utli_obj.read_file(file_f))
            print("data in file is {}" .format(data))
            count +=1
            if count==5:
                break
    '''    
        #class_folder[class_count]=folder
   # utli_obj.write_csv_file(data,class_folder)    

    
    
    
    
    
    

if __name__ == "__main__":
    main()