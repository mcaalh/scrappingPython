import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
	address = raw_input("enter location: ")
	if len(address) < 1 : break
	url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
	print 'Retrieving ', url
	uh = urllib.urlopen(url)
	data  = uh.read()
	print 'Retrieved', len(data), 'characters'

	try:
		js = json.loads(str(data))
	except:
		js = None

	if 'status' not in js or js['status'] != 'OK':
		print '===failure to retrieve===='
		print data
		# continue

	print json.dumps(js, indent = 4)
	lat = js["results"][0]["geometry"]["location"]["lat"]
	location = js["results"][0]["formatted_address"]

	print "latitude ", lat, "address ", location 