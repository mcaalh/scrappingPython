import urllib
from BeautifulSoup import *
url = raw_input("entrez l adresse web: ")
if len(url) < 1 : url = "http://python-data.dr-chuck.net/comments_197937.html"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
#retrieve a list of the anchor tags
#each tags is like a dictionary of html attributes
nums = list()
tags = soup('span')
for tag in tags:
	num = int(tag.contents[0])
	nums.append(num)

for i in xrange(5):
	print sum(nums)
