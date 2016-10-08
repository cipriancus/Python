def gcd(a,b):
    if b != 1:
        while b != a:
            if a>b:
                a=a-b;
            else:
                b=b-a;
        return a;
    else:
        return b;






def divizorComun(*list_of_params):
    greatestCurrentDivizor=gcd(list_of_params[0],list_of_params[1]);
    for iterator in range(2,len(list_of_params)):
        greatestCurrentDivizor=gcd(list_of_params[iterator],greatestCurrentDivizor);
    return greatestCurrentDivizor;


print(divizorComun(10,2,2));