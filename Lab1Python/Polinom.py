def polinom(x, sirPolinom):
    valoare=0;

    iterator=0;
    while iterator<len(sirPolinom):
        if sirPolinom[iterator].number():

            parametre=sirPolinom[iterator]*10;
            iterator=iterator+1;

                while iterator<len(sirPolinom):
                    if sirPolinom[iterator].number():
                        parametre=parametre*10+sirPolinom[iterator];
                        iterator = iterator + 1;
                    else:
                        if sirPolinom[iterator] == 'x':
                            parametre=parametre*x;
                            iterator = iterator + 1;
                        elif sirPolinom[iterator] == '^':
                              parametre=parametre**sirPolinom[iterator+1];
                              iterator=iterator+1;
                        elif sirPolinom[iterator]=='+':
                                valoare=valoare+parametre;
                                parametre=0;
                                iterator = iterator + 1;
                        else:
                            if sirPolinom[iterator]=='-':
                                valoare=valoare-parametre;
                                parametre=0;
                                iterator = iterator + 1;



