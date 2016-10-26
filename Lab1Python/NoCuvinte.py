def noCuvinte(sir):
    cuvant=0;
    previousCH="";
    for iterator in sir:
        if previousCH not in ", ;,?!." and iterator in ", ;,?!.":
            cuvant=cuvant+1
        previousCH = iterator

    return cuvant



print(noCuvinte(" ciprian e,,,ana    e; "));