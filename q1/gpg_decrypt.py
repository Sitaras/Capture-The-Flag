import os
import hashlib

file = open("keys.txt", "r")
keys = file.read().splitlines()

for key in keys:
    encrypted_key = hashlib.sha256(key.encode())
    encrypted_key = encrypted_key.hexdigest()
    stream = os.popen('gpg -d --passphrase '+encrypted_key+' --batch signal.log.gpg 2> /dev/null')
    # stream = os.popen('gpg -d --passphrase '+encrypted_key+' --batch firefox.log.gz.gpg | zcat 2> /dev/null')
    output = stream.read()
    lines = len(output.splitlines( ))
    if(lines > 0):
        print("found key: "+str(encrypted_key))
        break
