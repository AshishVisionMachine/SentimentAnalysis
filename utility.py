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
    
    def file_open(self,filename):
        file_f = open(filename, "r")
        
        return file_f
        
        
    def read_file(seld,filehandle):
        data=filehandle.read()
        return data
    
    def read_line(seld,filehandle):
        line_Data=filehandle.readline()
        return line_Data
    
    #def file_write(self,file_name):
    
        