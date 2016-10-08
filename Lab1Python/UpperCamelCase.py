def UpperCamelCase(sir):
    iterator=0;
    upper_nr=0;
    while iterator < len(sir):
        if sir[iterator].isupper():
            if upper_nr == 0:
                upper_nr=upper_nr+1;
            else:
                sir=sir[:iterator]+'_'+sir[iterator:];
                iterator=iterator+1;
        iterator = iterator + 1;
    sir.lower();
    return sir;


print(UpperCamelCase("AndreiAre"));

