def numara_caractere(text,tuplu_caractere):
    ch_dictionary=dict()

    for iterator in text:
        if iterator in tuplu_caractere:
            if iterator in ch_dictionary.keys():
                ch_dictionary[iterator]=ch_dictionary[iterator]+1
            else:
                ch_dictionary[iterator]=1

    nr_total=0
    for iterator in ch_dictionary.keys():
        nr_total=nr_total+ch_dictionary[iterator]

    return nr_total



print(numara_caractere("Python is awesome", ("e", "o")))