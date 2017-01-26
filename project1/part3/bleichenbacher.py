from roots import integer_nthroot, integer_to_base64
import hashlib
import sys
message = sys.argv[1]

def get_bytes(input_str):
    return len(input_str) / 2

def print_hex(input_str):
    print("0x%x" % int(input_str, 16))

#Public key consists of modulus n and public exponent e
#I used the 'useful command' to pull out the modulus from the
#bank public key

#Public key from National Bank of EECS388
e = 3

#For a  2048-bit key, the correct padding for an RSA signature
#using a SHA-1 hash should be 2048/8 - 32 = 218 bytes of FFs
#However, if we only use one FF, then there are 217 bytes at the end
#of the signature that we can use

#Under the hood, for a SHA-1 hash signed by a k-bit RSA key, the signed value
#will contain 00 01 | FF*(k/8 - 38 bytes) | ASN.1 Magic bytes denoting type of hash alg | SHA-1 digest

start = '0001'
frenchfries = 'ff' 
middle = '00'
asn1 = '3021300906052B0E03021A05000414'
garbage = 'ff' * 217

m = hashlib.sha1()
m.update(message)
mhash = m.hexdigest()

full = start + frenchfries + middle + asn1 + mhash 
#Full key is 2048 bits, so 256 bytes
#One hex digit = 4 bits, 2 hex digits = 8 bits = 1 byte
#print get_bytes(full) 
#print_hex(full)
#39 bytes, so 217 bytes left over that we can mess with
toforge = full + garbage
#print get_bytes(toforge)
#print_hex(toforge)

#Calculate cube root, will be non integer
from roots import integer_nthroot
forged_signature = integer_nthroot(int(toforge, 16), 3)[0]
#print forged_signature
#print "0x%x" % pow(forged_signature, 3)

print integer_to_base64(forged_signature)
