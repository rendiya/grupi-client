import urllib2
import json
import time
##import your gpio library

while True:
	response = urllib2.urlopen('https://api.grupi.org/blink/')
	data = json.load(response)
	dataget = data['response']['gpio']['gpio1']
	#print dataget
	if dataget == "1":
		print "nyala"
		##input nyala gpio disini
		#status high
	else:
		print "mati"
		##input mati gpio disini
		#status low
	time.sleep(5)
