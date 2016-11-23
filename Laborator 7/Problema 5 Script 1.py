import os
import json


def get_all_files(file_path):
    if os.path.isdir(file_path)==False:
        raise Exception("Path should be folder")
    else:
        all_files_list=list()

        for(root,directories,folders) in os.walk(file_path):
            for iterator in folders:
                all_files_list.append(os.path.join(root,iterator))

            for iterator in directories:
                temp_list=get_all_files(os.path.join(root,iterator))

                if len(temp_list)>0:
                    for iterator in temp_list:
                        all_files_list.append(iterator)
        return all_files_list


def write_all_files_in_folder(file_path):

    all_file_list=get_all_files(file_path)
    json_string=json.dumps(all_file_list)

    open("D:\\a.txt","wt").write(json_string)

write_all_files_in_folder("D:\\Seriale")
