def is_prime(number):
    for iterator in range(2, number // 2):
        if number % iterator == 0:
            return 0;

    return 1;


def prime(list_param):
    x = list()

    for iterator in list_param:
        if is_prime(iterator) == 1:
            x.append(iterator)

    return x


x = [1, 12, 13, 17]
print(prime(x))
