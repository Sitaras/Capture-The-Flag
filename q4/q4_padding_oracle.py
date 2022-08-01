#!/usr/bin/env python3
import subprocess
import time
import sys,os

# Message to decrypt: ad8bb176da1f40a98385ad0ae9777c3208b78ae57a7fec84092b2cbbaf2ab1c0


BLOCK_SIZE = 128
BYTE_NB = BLOCK_SIZE//8

IV = '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
request_count = 0 # total requests made to the oracle

def my_oracle(text):
    text = text.hex() # convert to hex
    global request_count   # count the curl requests
    request_count = request_count+1
    if request_count%100 == 0:
        print("Requests made: "+str(request_count)+" (out of 3384)")
    error_happened = 0
    while True:
        # the curl command that "asks" the oracle of the tor website
        curl_command = "curl --socks5-hostname localhost:9050 -v 'http://xtfbiszfeilgi672ted7hmuq5v7v3zbitdrzvveg2qvtz4ar5jndnxad.onion/check_secret.html' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed  -H 'Content-Type: application/x-www-form-urlencoded' -H 'Authorization: Basic YWRtaW46aGFtbWVydGltZQ==' -H 'Connection: close' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-User: ?1' --data-raw 'secret="+text+"&submit=go'"
        # exetute the curl request
        status, out = subprocess.getstatusoutput(curl_command)

        if "padding" in out:   # wrong padding
            return False
        elif "wrong secret" in out or "secret ok" in out:   # correct padding
            return True
        else:   # an error occured during the curl request
            # if an error happened, wait some secs and repeat the request
            error_happened = error_happened +1
            time.sleep(error_happened)

def poc(encrypted):
    block_number = len(encrypted)//BYTE_NB
    decrypted = bytes()
    # Go through each block
    for i in range(block_number, 0, -1):
        current_encrypted_block = encrypted[(i-1)*BYTE_NB:(i)*BYTE_NB]

        # At the first encrypted block, use the initialization vector if it is known
        if(i == 1):
            previous_encrypted_block = bytearray(IV.encode("ascii"))
        else:
            previous_encrypted_block = encrypted[(i-2)*BYTE_NB:(i-1)*BYTE_NB]

        bruteforce_block = previous_encrypted_block
        current_decrypted_block = bytearray(IV.encode("ascii"))
        padding = 0

        # Go through each byte of the block
        for j in range(BYTE_NB, 0, -1):
            padding += 1

            # Bruteforce byte value
            for value in range(0,256):
                bruteforce_block = bytearray(bruteforce_block)
                bruteforce_block[j-1] = (bruteforce_block[j-1] + 1) % 256
                joined_encrypted_block = bytes(bruteforce_block) + current_encrypted_block

                # Ask the oracle
                if(my_oracle(joined_encrypted_block)):
                    current_decrypted_block[-padding] = bruteforce_block[-padding] ^ previous_encrypted_block[-padding] ^ padding

                    # Prepare newly found byte values
                    for k in range(1, padding+1):
                        bruteforce_block[-k] = padding+1 ^ current_decrypted_block[-k] ^ previous_encrypted_block[-k]

                    break

        decrypted = bytes(current_decrypted_block) + bytes(decrypted)

    return decrypted[:-decrypted[-1]]  # Padding removal

#### Script ####

usage = """
Usage:
  python3 q4_padding_oracle.py <encrypted_message>
"""

if __name__ == '__main__':
    if len(sys.argv) == 2 : #chiffrement
        if len(sys.argv[1])%16!=0:       # code size security
            print(usage)
        else:
            x = poc(bytes.fromhex(sys.argv[1]))
            print("Decrypted message: ",x)
    else:
        print(usage)
