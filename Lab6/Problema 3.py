import re

def match_list(text,regExList):
    return_list=set()

    for iterator in regExList:
        if re.search(iterator,text):
            return_list.add(re.search(iterator,text).group(0))

    return return_list



print(match_list("andrei 23ana",["\w+","\d+"]))