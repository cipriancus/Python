import os
from pip._vendor.distlib.compat import raw_input


def parse(folder_path):

    if os.path.isfile(folder_path):
        raise Exception("A folder should be provided")

    if os.path.isdir(folder_path):
        try:
            list_dir=os.listdir(folder_path)

            for iterator in list_dir:
                next_path=os.path.join(folder_path,iterator)
                if os.path.isdir(next_path):
                    print(next_path)
                    parse(next_path)

        except PermissionError:
            print("No permission")

print(parse(raw_input("input path ")))