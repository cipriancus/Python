import os


def parse(file_path):
    try:
        if os.path.isfile(file_path) == True:
            raise Exception("Folder should be provided")

        else:
            file_dir = os.listdir(file_path)

            for iterator in file_dir:
                next_path = os.path.join(file_path, iterator)
                if os.path.isdir(next_path):
                    print(next_path)
                    parse(next_path)

    except PermissionError:
        print("No permission")


parse("D:\\")
