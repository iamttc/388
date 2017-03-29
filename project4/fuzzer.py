#!/user/bin/bash/python

import subprocess
import os
import base64
import sys
import random
import string


'''
Two ways to use:

    #Regular ascii
    python fuzzer.py | ./jsonParser

    #Base64
    python fuzzer.py
    cat fuzzInput.txt | base64 -d | ./jsonParser

'''

#####################
global depth

def depth_check():
    global depth
    if depth == 2:
        return 'DEEP'

def inc_depth():
    global depth
    depth += 1

def dec_depth():
    global depth
    depth -= 1

#####################

#####Helper functions###########
def get_int():
    return random.randint(0,10)

def get_chars():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(get_int()))

def get_true():
    return 'true'
    #return random.choice(['true', 'tru', 'tr', 'True', 'Tru', 'Tr', 'TRUE', 'TRU', 'TR'])

def get_false():
    return 'false'
    #return random.choice(['false', 'fals', 'fal', 'fa', 'False', 'Fals', 'Fal', 'Fa', 'FALSE', 'FALS', 'FAL', 'FA'])

def get_null():
    return 'null'
    #return random.choice(['null', 'nul', 'nu', 'Null', 'Nul', 'Nu', 'NULL', 'NUL', 'NU'])

def get_tuple():
    return '\"' + get_chars() + '\":' + get_value()
########################

##########Valid JSON###########
def get_object():
    if depth_check() == 'DEEP':
        return '{"":""}'
    inc_depth()

    obj = '{' + ','.join([get_tuple() for _ in range(0,3)]) + '}'

    dec_depth()
    return obj

def get_array():
    if depth_check() == 'DEEP':
        return '[]'
    inc_depth()

    array = '[' + ','.join([get_value() for i in range(0,3)]) + ']'

    dec_depth()
    return array

def get_value():
    return random.choice([get_string, get_number, get_object, get_array, get_true, get_false, get_null])()

def get_string():
    ##Can't handle any of these...
    #special = ['\\\"', '\\\\', '\\/', '\\b', '\\f', '\\n', '\\r', '\\t', '\\uaaaa']
    out = '\"'
    out += get_chars()
    #out += random.choice(special)
    out += '\"'
    return out

def get_number():
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    minus = '-'
    dot = '.'
    special = ['e', 'e+', 'e-', 'E', 'E+', 'E-']

    out = ""
    ##Apparently it can't handle this..
    #if bool(random.getrandbits(1)):
    #    out += minus

    num_max = 1000000
    for _ in range(0, random.randint(1, num_max)):
        out += random.choice(digits)

    if bool(random.getrandbits(1)):
        out += dot

    for _ in range(0, random.randint(1, num_max)):
        out += random.choice(digits)

    ##It has trouble with these
    #if bool(random.getrandbits(1)):
    #    out += random.choice(special)

    #    for _ in range(0, random.randint(1, 2)):
    #        out += random.choice(digits)

    return out

##############################

def main():
    global depth
    depth = 0

    with open('fuzzInput.txt', 'w') as f:
        while True:
            testcase = get_object()
            child = subprocess.Popen("./jsonParser", stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            _, stdErrOut = child.communicate(input = testcase)
            if child.returncode != 0 or stdErrOut != "":
                errMsg = stdErrOut.strip().split('\n')[0]
                out = base64.b64encode(testcase)
                f.write(out)
                print testcase
                exit(1);

                    


if __name__ == '__main__':
    main()
