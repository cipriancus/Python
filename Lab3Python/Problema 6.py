gDictionary={
    "+": lambda a, b: a + b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "%": lambda a, b: a % b
}

def apply_operator(operator,a,b):
    global gDictionary
    return gDictionary[operator](a,b)


print(apply_operator("*",3,4))