import requests,json,time


header = {'user-agent': 'grupi-bot/0.1','Content-type': 'application/json'}
data = {'id':'1','status':'on','alarm':'10:00','otomasi':'on'}
payload = json.dumps(data)
url = 'https://api.grupi.org/stable/tutorial/remote'
r = requests.post(url,headers=header,data=payload)
data = json.loads(r.text)

print data['response']['status']
