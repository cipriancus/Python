def intersectie(a, b):
    x=set()
    y=set()

    for iterator in a:
        x.add(iterator)

    for iterator in b:
        y.add(iterator)

    x=x.intersection(y)
    return x


def reuniune(a, b):
    x=set()
    x=x.union(a,b)
    return x


def minus(a, b):
    x=set()
    y = set()

    for iterator in a:
        x.add(iterator)

    for iterator in b:
        y.add(iterator)

    return x.difference(y)

a=[1,2,3,4]
b=[2,3,5]

print(intersectie(a,b))
print(reuniune(a,b))
print(minus(a,b))