def notin(a):
    global x;
    if a not in x:
        return a;

def aREUNITb(a,b):
    return list(filter(notin,a));

a=[1,2,3,4];
b=[2,5];

x=a;

print(aREUNITb(a,b));