def vocale(sir):
    sirVocale="aeiou";

    sir=sir.lower();

    for iterator in sir:
        if sirVocale.__contains__(iterator):
            return 1;

    return 0;


print(vocale("sss"));

