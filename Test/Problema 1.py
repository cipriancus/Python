def baza(l,b):
    new_str=""
    for iterator in l:
        new_str=new_str+str(iterator)

    return int(new_str,b)



print(baza([1,1],2))

print(baza([1,1,0],5))