# 3. Gasiti toate fisierele duplicate dintr-un director dat ca argument si afisati timpul de rulare.
# Calea grupurilor de fisiere duplicate vor fi scrise intr-un fisier output.txt.
import os
import hashlib


def compute_hash_of_file(file):
    m = hashlib.sha1()
    f = open(file, "rb")

    while True:
        data = f.read(4096)
        if len(data) == 0:
            break
        m.update(data)
    f.close()
    return m.hexdigest()


def search_for_hash(dir_name, search_hash):
    found_duplicates = list()

    for (root, directories, files) in os.walk(dir_name):
        for file in files:
            file_one_hash = compute_hash_of_file(os.path.join(root,file))
            if file_one_hash == search_hash:
                found_duplicates.append(os.path.join(root,file))

        for dir in directories:
            found_duplicates.append(search_for_hash(os.path.join(root,dir), search_hash))

    return found_duplicates


def duplicate_file(dir_name):
    external_file_to_write = open("D:\\duplicates.txt", mode="w", buffering=-1)

    for (root, directories, files) in os.walk(dir_name):
        for file in files:
            file_hash = compute_hash_of_file(os.path.join(root, file))
            equals_to_file = search_for_hash(root, file_hash)

            equals_to_file.pop(0)

            if len(equals_to_file) > 0:
                external_file_to_write.write("\n")
                external_file_to_write.write(str(os.path.join(root, file)))
                external_file_to_write.write(" ")
                external_file_to_write.write(str(equals_to_file))
                external_file_to_write.write("\n")

        for director in directories:
            duplicate_file(os.path.join(root, director))


duplicate_file("D:\\Filme")
