import re
#nu e gata
def replace_function(match):
    string=match.group(0)
    for iterator in range(0,len(string)):
        if iterator % 2 == 1:
            string=string[:iterator-1]+'*'+string[iterator+1:]
    return string

def get_text_cenzurat(text_string):
    text_to_return = re.sub("(?<=\W)[aeiou][a-z0-9]*[aeiou](?=\W)", replace_function, text_string)
    return text_to_return


print(get_text_cenzurat("ipria este smecher"))
