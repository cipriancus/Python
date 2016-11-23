

import os
from pip._vendor.distlib.compat import raw_input


def parse_and_write(pathFile, pathDirectory, buff):
    if not os.path.isfile(pathFile):
        raise Exception("This path must be to a file")
    if not os.path.isdir(pathDirectory):
        raise Exception("This path must be to a directory")
    fileRead = open(pathFile, "r")
    fileWrite = open(pathDirectory + "/" + "a.txt", "wt")
    fileWrite.write(fileRead.read())

#full path : D:/Folder  D:/Folder/file.txt
try:
    args = raw_input("ENTER pathFile and pathDirectory and integer (separated by space): ")
    args = args.split(" ")
    if len(args) == 3:
        parse_and_write(args[0], args[1], args[2])
    else:
        raise Exception("3 arg: pathFile and pathDirectory and integer")
except:
    raise Exception("Something is wrong")
