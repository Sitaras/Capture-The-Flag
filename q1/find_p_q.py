import math


def isprime(num):
    for n in range(2, int(num**0.5)+1):
        if num % n == 0:
            return False
    return True


N = 127670779

square = math.sqrt(N)
square = math.ceil(square)
for i in range(3, square+1):
    if isprime(i) and ((N % i) == 0):
        print("found p="+str(i)+"  q="+str(int(N/i)))
