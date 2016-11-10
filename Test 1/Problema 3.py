def rep(key,cuvant,sir):
    return sir.replace("#"+key+"#",cuvant)


def rezolva_pattern(template,context):
    for iterator in context.keys():
        template=rep(iterator,context[iterator],template)
    return template


print(rezolva_pattern("hello #who#",{"who": "world"}))

print(rezolva_pattern("Dont {{do}} this #do#",{"do": ", seriously"}))

print(rezolva_pattern("I am #action# #language#",{"action":"learning", "language": "Python"}))

