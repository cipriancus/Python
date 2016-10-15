import math;

x=[1,2,3,4];
y=x;

def nrcombinari(x,k):
    return math.factorial((len(x)))//((math.factorial((len(x)))-math.factorial(k))*math.factorial(k));

def comb(n,r):
    k=nrcombinari(x,r);

    global y;

    if k==0:
        y=x;
        print(y);
    else:
        i=k-1;
        while i>=0:
            a=y[i];
            y[i]=y[k-1];
            y[k-1]=a;

            comb(k-1,r);

            a = y[i];
            y[i] = y[k - 1];
            y[k - 1] = a;

            i=i-1;

comb(len(x),3);