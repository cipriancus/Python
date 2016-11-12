import re


def match(regex, text, x):
    list_of_substrings = re.findall(regex, text)

    return_list = list()

    for iterator in list_of_substrings:
        if len(iterator) == x:
            return_list.append(iterator)

    return return_list


print(match("\w+", "ana are mere", 3))
