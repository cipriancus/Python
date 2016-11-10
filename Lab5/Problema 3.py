import os
from pip._vendor.distlib.compat import raw_input

def writeENV(file_path):

    if os.path.isfile(file_path) != True:
        raise Exception("Path does not point to a file")

    file=open(file_path,mode='w',buffering=-1)

    os_eviron=os.environ
    for iterator in os_eviron.keys():
        file.writelines(str(iterator)+":"+str(os_eviron[iterator])+"\n")



print(writeENV(raw_input("input")))
