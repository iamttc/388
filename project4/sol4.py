#!/user/bin/bash/python

count = 3
ints = [6, 6, 6]

out = str(bin(count)[2:].zfill(32)) + " " + " ".join([str(bin(x)[2:].zfill(32)) for x in ints])
print out
