import re

def cenzura(text):
    string_vocale=re.findall("(\W[aeiou]\W)|(\W[aeiou]\w*[aeiou]\W)|(^[aeiou]\w*[aeiou]\W)|(\W[aeiou]\w*[aeiou]$)",text)
    return string_vocale


print(cenzura("aipria este smecher"))