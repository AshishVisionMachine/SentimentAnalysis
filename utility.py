
import os
class utility:
    def __init__(self,init="default"):
        self.init=init
        
    def get_path(self,folder_name):
    
        dir_path=os.path.abspath(folder_name)
        
        return dir_path
    
    
    def get_file_list(self,dir_path):
        file_list=os.listdir(dir_path)
        
        return file_list
    