import urllib2
import re

urlInfo = "localhost:8000"

r = re.compile("<li><a\shref=\"[^\"\.]*\.py\">(([A-Za-z])+\.py)<\/a>")

try:
	req = urllib2.Request('http://localhost:8000')
	response = urllib2.urlopen(req)
	the_page = response.read()

	for mo in r.finditer(the_page):
		print(mo.group(0))
		print(mo.group(1))
		
except Exception as e:
	print ("Error -> ",e)