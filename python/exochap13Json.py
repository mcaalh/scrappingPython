import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
	address = raw_input("enter location: ")
	if len(address) < 1 : break
	url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
	print 'Retrieving ', url
	uh = urllib.urlopen(url)
	data  = uh.read()

	js = json.loads(str(data))


	if 'status' not in js or js['status'] != 'OK':
		print '===failure to retrieve===='
		print data
		continue

	idd = js["results"][0]["place_id"]
	print idd
