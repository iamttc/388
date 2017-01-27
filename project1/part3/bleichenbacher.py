from roots import integer_nthroot, integer_to_base64
import hashlib
import sys
message = sys.argv[1]

def get_bytes(input_str):
    return len(input_str) / 2

def print_hex(input_str):
    print("0x%x" % int(input_str, 16))

# public key from National Bank of EECS388
# public key consists of modulus n and public exponent e
e = 3

# for a  2048-bit key, the correct padding for an RSA signature
# using a SHA-1 hash should be 2048/8 - 32 = 218 bytes of FFs
# 00 01 | FF*(k/8 - 38 bytes) | ASN.1 Magic bytes denoting type of hash alg | SHA-1 digest
start = '0001'
frenchfries = 'ff'
middle = '00'
asn1 = '3021300906052B0E03021A05000414'
garbage = 'ff' * 217

# hash
m = hashlib.sha1()
m.update(message)
mhash = m.hexdigest()

full = start + frenchfries + middle + asn1 + mhash
toforge = full + garbage

# calculate cube root, will be non integer
from roots import integer_nthroot
forged_signature = integer_nthroot(int(toforge, 16), 65536)[0]

print integer_to_base64(forged_signature)
