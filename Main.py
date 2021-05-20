from Preprocessing import preprocessing 
from utility import utility
import os
input_string="I am , feeling Good today"
test_string="Hi"
folder_path ="tokens"

def main():
    print("test main function ")
    obj=preprocessing(test_string)
    
    input=obj.lowercasing(input_string)
    print("lower case word is {}".format(input))
    
    stop_input=obj.stopwordemoval(input)
    
    print("stop result is {}".format(stop_input))
    
    utli_obj=utility()
    print(utli_obj.get_path(folder_path))
    
    path=utli_obj.get_path(folder_path)
    
    print(utli_obj.get_file_list(path))
    
    for folder in utli_obj.get_file_list(path):
        print("list of file is {}".format(utli_obj.get_file_list(os.path.join(path,folder))))
    
    
    
    
    
    

if __name__ == "__main__":
    main()