def lista(y,*listOfLists):
    x=dict()

    for iterator in listOfLists:
        for iterator2 in iterator:
            if iterator2 in x.keys():
                x[iterator2]=x[iterator2]+1
            else:
                x[iterator2]=1

    items=list()

    for iterator in x.keys():
        if x[iterator] == y:
            items.append(iterator)
    return items


print(lista(2,[1,2,3], [2,3,4], [4,5,6], [4, 1, "test"]))