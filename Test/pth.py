def funct(str):
    exec(str)
    return suma(4,3)

print(funct("def suma(a,b): return a+b"))