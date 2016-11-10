def reuniune_intervale(list_of_touples):
    reunion_list=set()

    for iterator in list_of_touples:
        for iterator2 in range(iterator[0],iterator[1]+1):
            if iterator2 in reunion_list:
                reunion_list.remove(iterator2)
            else:
                reunion_list.add(iterator2)

    return reunion_list



print(reuniune_intervale([(2,4),(5,8),(7,12)]))