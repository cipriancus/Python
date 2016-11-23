import os
import re


def parsing(folder_path, regex):
    found_files = list()

    if os.path.isdir(folder_path) == False:
        raise Exception("Not a folder")
    else:
        for (root, directories, files) in os.walk(folder_path):
            for iterator in files:
                name = os.path.basename(os.path.join(root, iterator))
                found_match = False
                found_match_substring = False

                if re.match(regex, name):
                    found_match = True

                if re.search(regex, name):
                    found_match_substring = True

                if found_match == found_match_substring == True:
                    found_files.append(">>" + str(os.path.join(root, iterator)))
                elif found_match_substring != found_match and (found_match == True or found_match_substring == True):
                    found_files.append(">" + str(os.path.join(root, iterator)))

            for iterator in directories:
                temporary_list = parsing(os.path.join(root, iterator),regex)

                if len(temporary_list) > 0:
                    for iterator in temporary_list:
                        found_files.append(iterator)

    return found_files


print(parsing("D:\\Kituri", "[a-zA-Z]"))
