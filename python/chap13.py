import urllib
import xml.etree.ElementTree as ET
url = raw_input("entrez l adresse web: ")
if len(url) < 1 : url = "http://python-data.dr-chuck.net/comments_197934.xml"
exml = urllib.urlopen(url).read()
stuff = ET.fromstring(exml)
lst = stuff.findall('comments/comment')
countcom = list()

for thing in lst:
	com = int(thing.find('count').text)
	countcom.append(com)

print sum(countcom)

