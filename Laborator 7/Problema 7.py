import random

def saseDINpatruzecisinoua():
    selected_numbers=set()

    while len(selected_numbers)!=6:
        selected_numbers.add(random.randint(1,49))

    return selected_numbers


print(saseDINpatruzecisinoua())