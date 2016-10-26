def fazan(char_len,*list_of_siruri):
    for iterator in range(0,len(list_of_siruri)-1):
        if list_of_siruri[iterator][-char_len:] != list_of_siruri[iterator+1][0:char_len]:
            return 0;
    return 1;



print(fazan(2,"ciprian","andri","eida"));