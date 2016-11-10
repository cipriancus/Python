def seturi(II,n):
    new_set=set()

    dictionary=dict()

    for iterator in II:
        if iterator in dictionary.keys():
            dictionary[iterator]=dictionary[iterator]+1
        else:
            dictionary[iterator]=1

    for iterator in dictionary.keys():
        if dictionary[iterator] == n:
            new_set.add(iterator)


    return new_set


print(seturi("12333241",2))
print(seturi(".1234", 3))
print(seturi(".1234.",1))