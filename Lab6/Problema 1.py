import re

def extragere(text):
    return re.findall("\w+",text);

print(extragere("ana are mere"));