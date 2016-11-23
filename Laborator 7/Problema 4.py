#. Sa se scrie un script care primeste ca argument un director si creeaza un fisier JSON cu date despre toate fisierele din acel director.
# Pentru fiecare fisier vor fi afisate urmatoarele informatii:
# nume_fisier, md5_fisier, sha256_fisier, size_fisier (in bytes),
# cand a fost creat fisierul (in format human-readable) si calea absoluta catre fisier.
import hashlib
import os
import json

def compute_sha1(file):
    m = hashlib.sha1()
    f = open(file, "rb")

    while True:
        data = f.read(4096)
        if len(data) == 0:
            break
        m.update(data)
    f.close()
    return m.hexdigest()

def compute_sha256(file):
    m = hashlib.sha256()
    f = open(file, "rb")

    while True:
        data = f.read(4096)
        if len(data) == 0:
            break
        m.update(data)
    f.close()
    return m.hexdigest()

def compute_md5(file):
    m = hashlib.md5()
    f = open(file, "rb")

    while True:
        data = f.read(4096)
        if len(data) == 0:
            break
        m.update(data)
    f.close()
    return m.hexdigest()


def write_json(folder_path):
    if os.path.isfile(folder_path)==False:
        raise Exception("Not a file")
    else:
        dictionary=dict()
        dictionary["md5_fisier"]=compute_md5(folder_path)
        dictionary["sha1_fisier"] = compute_sha1(folder_path)
        dictionary["sha256_fisier"] = compute_sha256(folder_path)
        dictionary["size_fisier"]=os.path.getsize(folder_path)
        dictionary["nume_fisier"]=os.path.basename(folder_path)

        data=json.dumps(dictionary)
        return data

print(write_json("D:\\a.txt"))

