from Preprocessing import preprocessing 

input_string="I am feeling Good today"
test_string="Hi"

def main():
    print("test main function ")
    obj=preprocessing(test_string)
    
    input=obj.lowercasing(input_string)
    print(input)
    
    token_input=obj.stopwordemoval(input)
    
    print(token_input)
    

if __name__ == "__main__":
    main()