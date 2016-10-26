def vocale(sir):
    sirVocale="aeiou";

    sir=sir.lower();

    for iterator in sir:
        if iterator in sirVocale:
            return 1;

    return 0;


print(vocale("a"));

