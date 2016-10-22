def numarare(sir_caractere):
    ch_map = dict();
    for iterator in sir_caractere:
        if iterator in ch_map.keys():
            number = ch_map[iterator] + 1
            ch_map[iterator] = number
        else:
            ch_map[iterator] = 1
    return ch_map

print(numarare("abca"))