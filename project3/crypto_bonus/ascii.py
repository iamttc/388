import sys
import binascii

def xor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

file1 = binascii.hexlify(open(sys.argv[1], 'rb').read()).decode('hex')
file2 = binascii.hexlify(open(sys.argv[2], 'rb').read()).decode('hex')

file3 = xor(file1, file2).encode('hex')

open(sys.argv[3], 'wb').write(file3)
