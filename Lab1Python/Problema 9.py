def is_prime(number):
    for iterator in range(2,number//2):
        if number % iterator==0:
            return 0;

    return 1;


def parse(string):
    maxPrime=0

    previousNO=""

    for iterator in string:
        if iterator.isalpha()== False:
            previousNO=previousNO+iterator;
        else:
            if len(previousNO)>0:
                if is_prime(int(previousNO))==1 and int(previousNO)>maxPrime:
                    maxPrime=int(previousNO)
            previousNO=""


    return maxPrime;

print(parse("ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda"))