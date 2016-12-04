import os
import hashlib
import time
import json


def md5_file(file):
    if os.path.isfile(file) == False:
        raise Exception("Not a file")
    else:
        m = hashlib.md5()
        f = open(file, "rb").read()
        m.update(f)
        return m.hexdirest()


def sha1_file(file):
    if os.path.isfile(file) == False:
        raise Exception("Not a file")
    else:
        m = hashlib.sha1()
        f = open(file, "rb").read()
        m.update(f)
        return m.hexdirest()


def parse_directory(path):
    md5_dict = dict()
    sha1_dict = dict()

    if os.path.isdir(path) == False:
        raise FileNotFoundError("Not a folder")
    else:
        for (root, directory, folders) in os.walk(path):
            for iterator in directory:
                (md5_temporary, sha1_temporary) = parse_directory(os.path.join(root, iterator))

                if len(md5_temporary) > 0 and len(sha1_temporary) > 0:
                    for iterator1 in md5_temporary.keys():
                        md5_dict[os.path.join(root, iterator1)] = md5_temporary[iterator1]
                    for iterator1 in md5_temporary.keys():
                        sha1_dict[os.path.join(root, iterator1)] = md5_temporary[iterator1]

            for iterator in folders:
                md5_file = md5_file(os.path.join(root, iterator))
                sha1_file = sha1_file(os.path.join(root, iterator))

                md5_dict[os.path.join(root, iterator)] = md5_file
                sha1_dict[os.path.join(root, iterator)] = sha1_file

        return (md5_dict, sha1_dict)


def write_json(path):
    try:
        (md5_dict, sha1_dict) = parse_directory(path)

        join_list = list()

        for iterator in md5_dict.keys():  # au aceleasi chei
            temp_list = list()
            temp_list.add(md5_dict[iterator])
            temp_list.add(sha1_dict[iterator])
            temp_list.add(os.path.basename(iterator))
            join_list.add(temp_list)

        s = json.dumps(join_list)
        open("output.json", "wt").write(s)

    except FileNotFoundError:
        print("File not found")
    except:
        print("error")


def cout_time(path):
    try:
        start = time.time()
        write_json(path)
        end = time.time()
        print(end - start)
    except Exception:
        print(Exception)


try:
    input=input("Enter path")

    if len(input)>0:
        write_json(input)
    else:
        raise Exception("invalid params")

except Exception:
    print(Exception)