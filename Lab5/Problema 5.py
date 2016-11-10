import os



def parse_and_write(directory_path,file_path):

    walk_result=os.walk(file_path)

    file=open(file_path,mode='r',buffering=-1)

    for iterator in walk_result:
        print("da")




parse_and_write("D:\\","D:\\a.txt")