import base64
def encrypt(key, msg):
    encryped = []
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        encryped.append(chr((msg_c + key_c) % 127))
    return ''.join(encryped)

def decrypt(key, encryped):
    msg = []
    for i, c in enumerate(encryped):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        msg.append(chr((enc_c - key_c) % 127))
    return ''.join(msg)
import json
payload = {'suhu': 23, 'waktu': '10-10-2016 14:34','nama':'raspberry_pi'}
jsdata = json.dumps(payload)


if __name__ == '__main__':
    key = 'my_device_raspberry'
    msg = jsdata
    encrypted = repr(encrypt(key, msg))
    decrypted = decrypt(key, eval(encrypted))
    kompres = base64.b64encode(encrypted)
    dekompres = base64.b64decode(kompres)
    decrypted2 = decrypt(key, eval(dekompres))

    print "pesan: ",msg
    print "kunci: ",key
    print "enkripsi: ",encrypted
    print "dekripsi: ",decrypted
    print "kompres base64: ",kompres
    print "dekompres: ",dekompres
#    print decrypted2
