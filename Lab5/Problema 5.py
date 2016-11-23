import os
from pip._vendor.distlib.compat import raw_input

def parse_and_write(directory_path, file_path):
    if os.path.isdir(directory_path) == False:
        raise Exception("Path should be file")

    if os.path.isfile(file_path) == False:
        raise Exception("File is not valid")
    else:
        write_in_file = open(file_path, mode="a", buffering=-1)

    for (root, directories, files) in os.walk(directory_path):

        for iterator in directories:
            write_in_file.write(str(os.path.join(root, iterator)) + "|" + "DIRECTORY\n")
            parse_and_write(os.path.join(root, iterator), file_path)

        for iterator in files:
            write_in_file.write(str(os.path.join(root, iterator)) + "|" + "FILE\n")


#full path : D:/Folder  D:/Folder/file.txt
try:
    args = raw_input("ENTER PATH and file (separated by space): ")
    args = args.split(" ")
    parse_and_write(args[0], args[1])
except:
    raise Exception("Something is wrong")

#parse_and_write("D:\\Seriale", "D:\\a.txt")
