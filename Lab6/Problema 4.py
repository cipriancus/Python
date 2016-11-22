import os
import re

#{"class": "url", "name": "url-form", "data-id": "item"}
#class="url" si name="url-form" si data-id="item"

def open_path(path):
    folder=open(path,mode='r',buffering=-1)
    return folder.read()

def xml_dictionar(path,attr):
    text=open_path(path)

    selected_list=list()

    for iterator in attr.keys():
        find=re.findall(str(iterator)+"="+str(attr.get(iterator)),text)
        selected_list.append(find)

    return selected_list


print(xml_dictionar("D:\\a.xml",{"class": "url", "name": "url-form", "data-id": "item"} ))