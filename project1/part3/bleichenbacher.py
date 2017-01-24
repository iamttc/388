#Lazy implementaiton + modulus 3, lets you create valid signature
#See discussion slides
from roots import *
import hashlib
import sys
#message = sys.argv[1]
message = '50cent+hirochri+0.50'


#Public key consists of modulus n and public exponent e
#I used the 'useful command' to pull out the modulus from the
#bank public key

#Public key from National Bank of EECS388
n = 0x00b06004b3528bfd2d187f48e6cb9f3fe79afade6cc3c428dd0577b8bb3e752824b632d100d28b396726a887c5189ded3fe9717d959730dadbf468b2bc76eea3c15091a38b61fdfa46b1510ef885ea3105ae7d7f3007e97c6761bc47e715ba32464c77f7d0cfd2c88c0f53d45404a110d6951d3f4255edc3523921237a86f35fed200c7e45870b822d7652dc896d0de064617dbb48eb9b1d47103f12911b0dab3d91e0fdb847f0b87cf2b20b19d3b951cae86cab611893f6f4cd016c68607e970fc2db800f981d9bb4441fe5d70299693a8ae51f2e9b2656f0c279bf87ecb96a753f231739eb1f9a9d7dd01f15f283dd2da2887e7fdef6aedd61c4ca7b3be1b1cd
e = 3

#For a  2048-bit key, the correct padding for an RSA signature
#using a SHA-1 hash should be 2048/8 - 32 = 218 bytes of FFs
#However, if we only use one FF, then there are 217 bytes at the end
#of the signature that we can use

#Under the hood, for a SHA-1 hash signed by a k-bit RSA key, the signed value
#will contain 00 01 | FF*(k/8 - 38 bytes) | ASN.1 Magic bytes denoting type of hash alg | SHA-1 digest

def get_bytes(input_str):
    return len(input_str) / 2

def print_hex(input_str):
    print("0x%x" % int(input_str, 16))

start = '0001'
frenchfries = 'ff' 
middle = '00'
asn1 = '3021300906052B0E03021A05000414'
garbage = 'ff' * 217

import hashlib
m = hashlib.sha1()
m.update(message)
mhash = m.hexdigest()

full = start + frenchfries + middle + asn1 + mhash 
#Full key is 2048 bits, so 256 bytes
#One hex digit = 4 bits, 2 hex digits = 8 bits = 1 byte
print get_bytes(full) 
print_hex(full)
#39 bytes, so 217 bytes left over that we can mess with
toforge = full + garbage
print get_bytes(toforge)
print_hex(toforge)

#Calculate cube root, will be non integer
from roots import integer_nthroot
cube_root = integer_nthroot(int(toforge, 16), 3)[0]
print cube_root
print "0x%x" % pow(cube_root, 3)
#Round cube root?
forged_signature = cube_root

print integer_to_base64(forged_signature)
