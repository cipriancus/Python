import os


def get_file_info(file_path):
    if os.path.isfile(file_path):
        return_dictionary = dict()
        return_dictionary["full_path"] = file_path
        return_dictionary["file_size "]=os.path.getsize(file_path)

        filename,file_extension=os.path.splitext(file_path)

        return_dictionary["file_extension"]=file_extension
        return_dictionary["can_read"]=os.access(file_path,os.R_OK)
        return_dictionary["can_write"]=os.access(file_path,os.W_OK)

        return_dictionary
    else:
        raise Exception("Not a file")


print(get_file_info("D:\\a.txt"))