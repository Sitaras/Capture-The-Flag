# requires python 3.8 or newer
def moduldar_inverse(a, m):
    return pow(a, -1, m)


p = 7963  # found using find_p_q.py
q = 16033   # found using find_p_q.py
e = 7   # given
encrypted_x = 32959265   # given
encrypted_y = 47487400   # given
phi = (p-1)*(q-1)
N = p*q
d = moduldar_inverse(e, phi)

decrypted_x = pow(encrypted_x, d, N)
decrypted_y = pow(encrypted_y, d, N)

print("encrypted_x= " + str(encrypted_x) + " || decrypted_x= " + str(decrypted_x))
print("encrypted_y= " + str(encrypted_y) + " || decrypted_y= " + str(decrypted_y))
