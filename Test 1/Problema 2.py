def gaseste_asemanari(list_one,list_two):
    set_one=set()

    for iterator in list_one:
        for iterator2 in list_two:
            if str(iterator)==str(iterator2):
                set_one.add(iterator)

    return set_one


print(gaseste_asemanari([1,2,3,4,5,6,5,4,3,2,1], [1,1,2,2,3,3,4,5]))

print(gaseste_asemanari(["1", 2, None, None, True, "3"], ["None", None, True, 1, "1"]))