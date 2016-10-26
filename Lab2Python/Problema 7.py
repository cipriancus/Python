# Sa se scrie o functie care primeste ca parametri
# un numar x default egal cu 1, un numar variabil
# de siruri de caractere si un flag boolean setat default pe True.
# Pentru fiecare sir de caractere, sa se genereze o
# lista care sa contina caracterele care au codul
# ASCII divizibil cu x in caz ca flag-ul este setat pe True,
# in caz contrar sa contina caracterele care au codul ASCII
# nedivizibil cu x.
# Exemplu: x=2, "test", "hello", "lab002", flag=False va returna (["e", "s"], ["e", "o"], ["a"]).
# Atentie: functia trebuie sa returneze un numar variabil de
# liste care sa corespunda cu numarul de siruri de caractere primite ca input.

def compare(number, x, flag):
    if flag == True:
        if number % x == 0:
            return True

    if flag == False:
         if number % x != 0:
            return True

    return False


def division(x=1, flag=True, *list_of_string):
    selected_strings = list()

    for iterator in list_of_string:
        temList = list()
        for iterator2 in iterator:
            if compare(ord(iterator2), x, flag):
                temList.append(iterator2)

        selected_strings.append(temList)

    return selected_strings



print(division(2,False, "test", "hello", "lab002"))