def addition(list):
    c=1;
    for iterator in list:
        c=c+iterator
    return c

def additionWithParam(number,list):
    c=1;
    for iterator in list:
        c=c+iterator+number
    return c