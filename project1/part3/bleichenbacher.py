#Lazy implementaiton + modulus 3, lets you create valid signature
#See discussion slides

from roots import *
import hashlib
import sys
message = sys.argv[1]

# Your code to forge a signature goes here.

print integer_to_base64(forged_signature)
