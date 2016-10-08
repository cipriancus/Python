def caractere(sir):

    caractereSpeciale="\\n''\t''\a''\b''\f''\b''\v'";

    if sir.__contains__(caractereSpeciale):
        return 1;


print(caractere("ciprian "));