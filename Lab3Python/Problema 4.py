def build_xml_element(tag,content,**value_key):
    name="<"+tag
    for iterator in value_key.keys():
        name=name+" "+iterator+"=\""+value_key[iterator]+"\""

    name=name+">"+content+"</"+tag+">"

    return name


print(build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))