import urllib
from BeautifulSoup import *
url = raw_input("entrez l adresse web: ")
if len(url) < 1 : url = "http://python-data.dr-chuck.net/known_by_Keerah.html"
count = int(raw_input("count: "))
pos = int(raw_input("position: "))

for i in xrange(count):
	
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)

	tags = soup('a')
	url = tags[pos-1].get('href')
	print url