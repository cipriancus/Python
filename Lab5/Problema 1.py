from pip._vendor.distlib.compat import raw_input

suma=lambda a,b:a+b
diferenta=lambda a,b:a-b
inmultire=lambda a,b:a*b

if b!=0:
    impartire=lambda a,b: a/b
else:
    raise ArithmeticError("b cannot be 0")

try:
    a=raw_input("write a")
    b=raw_input("write b")
except ValueError:
    print("Not a number")


print(suma(a,b))
print(diferenta(a,b))
print(inmultire(a,b))
print(impartire(a,b))
