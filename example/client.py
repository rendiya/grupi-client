import urllib2
import json
import time
##import your gpio library

while True:
	response = urllib2.urlopen('https://api.grupi.org/stable/tutorial/')
	print response
	data = json.load(response)
	print data
	dataget = data['response']['status']
	#print dataget
	if dataget == "on":
		print "nyala"
		##input nyala gpio disini
		#status high
	else:
		print "mati"
		##input mati gpio disini
		#status low
	time.sleep(5)
