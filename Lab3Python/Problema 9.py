
def operation(*list_of_sets):
    dictionary=dict()
    name = ""

    for iterator in list_of_sets:
        for iterator2 in list_of_sets:
            if iterator != iterator2:
                name = str(iterator) + "|" + str(iterator2)
                dictionary[name] = len(iterator.union(iterator2))

                name =str(iterator) + "&" + str(iterator2)
                dictionary[name] = len(iterator.intersection(iterator2))

                name=str(iterator)+"-"+str(iterator2)
                dictionary[name]=len(iterator.difference(iterator2))

    return dictionary

a={1,2,3,4,5}
b={1,2,3,4}
print(operation(a,b))