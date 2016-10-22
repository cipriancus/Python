from _operator import itemgetter


def getRuleNo(rule,dictionary_rules):
    for iterator in range(0,len(dictionary_rules)):
        if rule in dictionary_rules[iterator]:
            return iterator
    return -1

def getPosition(substring,string):
    if len(substring)==0:
        return -1;
    return string.find(substring)

def validate_dict(dictionary_rules,validate_dictionary):
    for iterator in validate_dictionary.keys():
        position=getRuleNo(iterator,dictionary_rules)
        if position != -1:
            prefix=dictionary_rules[position][1]
            middle=dictionary_rules[position][2]
            suffix=dictionary_rules[position][3]

            position_prefix=getPosition(prefix,validate_dictionary[iterator])
            position_middle=getPosition(middle,validate_dictionary[iterator])
            position_suffix=getPosition(suffix,validate_dictionary[iterator])

            if not(position_prefix<=position_middle<=position_suffix):
                return 0

        else:
            return 0

    return 1



print(validate_dict([("key1", "", "inside", ""),("key2", "start", "middle", "winter")],{"key2": "starting the engine in the middle of the winter", "key1": "come inside, it's too cold outside"}))

