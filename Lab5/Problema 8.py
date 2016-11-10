import os

def create_tree(path,tree_depth,filesize,filecout,dircount):

    if not os.path.exists(path):
        os.mkdir(path,mode=0o700)

        for iterator in range(0,tree_depth-1):


    else:
        raise Exception("Directory already in use")


create_tree("D:\\test",2,1024,3,3)