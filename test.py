from itsdangerous import Signer, URLSafeSerializer as urlsafe
import json
payload = {'suhu': 23, 'waktu': '10-10-2016 14:34','nama':'raspberry_pi'}
jsdata = json.dumps(payload)

s = urlsafe('generate:grupi.org')
b = s.dumps(jsdata)
#print s
print b
print s.loads(b)

import hashlib
hash_object = hashlib.md5(b'%s' %jsdata)
hex_dig = hash_object.hexdigest()
print(hex_dig)
