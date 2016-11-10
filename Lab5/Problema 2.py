#Scrieti un script care primeste ca parametru de la linia de comanda un path si afiseaza primii 4096 bytes
# daca path-ul duce la un fisier, intrarile din acesta daca path-ul reprezinta un director
# si un mesaj de eroare daca path-ul nu este unul valid.

import os
from pip._vendor.distlib.compat import raw_input

try:
    path=raw_input("ENTER PATH ")

    if os.path.isdir(path):
        print(os.listdir(path))

    elif os.path.isfile(path):
        FILE=open(path,mode='r',buffering=4096)
        print(FILE.read())
        
    else:
        raise FileNotFoundError

except FileNotFoundError:
    print("No path was found")