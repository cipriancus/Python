import os


def write_env(file_path):
    if os.path.isdir(file_path) == True:
        raise Exception("Path does not point to a file")

    else:

        file = open(file_path, mode="w", buffering=-1);

        for iterator in os.environ.keys():
            file.write(str(iterator) + ":" + str(os.environ[iterator]) + "\n");

        file.close()


print(write_env("D:\\ana.txt"))