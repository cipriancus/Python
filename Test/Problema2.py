def dictionare(dict1,dict2,x):
    return_set=set()

    for iterator in dict1.keys():
        if type(x)==type(dict1[iterator]):
            return_set.add(dict1[iterator])

    for iterator in dict2.keys():
        if type(x)==type(dict2[iterator]):
            return_set.add(dict2[iterator])

    return return_set


print(dictionare({1:2,3:4,"5":"6"},{0:0,(2,3):1,6:(2,4)}, 2))

print(dictionare({1:2,3:4,"5":"6"},{(1,2,3):0,1:(2,3),6:(2,4)}, (1,2)))