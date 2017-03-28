#!/user/bin/bash/python

import subprocess
import os
import base64
import sys
import random
import string

#####################
global depth

def depth_check():
    global depth
    if depth == 2:
        return 'FUCK'

def inc_depth():
    global depth
    depth += 1

def dec_depth():
    global depth
    depth -= 1

#####################

#####Random helper shit#########
def get_int():
    return random.randint(0,10)

def get_chars():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(get_int()))

def get_true():
    return random.choice(['true', 'tru', 'tr', 'True', 'Tru', 'Tr', 'TRUE', 'TRU', 'TR'])

def get_false():
    return random.choice(['false', 'fals', 'fal', 'fa', 'False', 'Fals', 'Fal', 'Fa', 'FALSE', 'FALS', 'FAL', 'FA'])

def get_null():
    return random.choice(['null', 'nul', 'nu', 'Null', 'Nul', 'Nu', 'NULL', 'NUL', 'NU'])

def get_tuple():
    return '\"' + get_chars() + '\":' + get_value()
########################


######All json objects#########
def get_object():
    if depth_check() == 'FUCK':
        return '{}'
    inc_depth()

    obj = '{'
    for x in range(get_int()):
        obj += get_tuple()
        obj += ','
    obj += '}'

    dec_depth()
    return obj

def get_array():
    if depth_check() == 'FUCK':
        return ''
    inc_depth()

    array = '['
    for i in range(0,4):
        rand = random.randint(0,4)
        if rand == 0:
            array += get_number()
        elif rand == 1:
            array += get_string()
        elif rand == 2:
            array += get_object()
        elif rand == 3:
            array += get_array()
        if i != 3:
            array += ','
    array += ']'

    dec_depth()
    return array

def get_value():
    return random.choice([get_string, get_number, get_object, get_array, get_true, get_false, get_null])()

def get_string():
    fukd = ['\\','','\\\\','\/','\b','\u','\u12fd','\uzxdg3'] # ,'\n', '\r', '\t', '\f'
    temp = '\"'
    temp += ''.join([random.choice(fukd) for _ in range(0, random.randint(0, 10))])
    temp += get_chars()
    temp += '\"'
    return temp

def get_number():
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    minus = '-'
    dot = '.'
    special = ['e', 'e+', 'e-', 'E', 'E+', 'E-']

    out = ""
    ##Apparently it can't handle this..
    #if bool(random.getrandbits(1)):
    #    out += minus

    for _ in range(0, random.randint(1, 3)):
        out += random.choice(digits)

    if bool(random.getrandbits(1)):
        out += dot

    for _ in range(0, random.randint(1, 5)):
        out += random.choice(digits)

    ##It has trouble with these
    #if bool(random.getrandbits(1)):
    #    out += random.choice(special)

    #    for _ in range(0, random.randint(1, 2)):
    #        out += random.choice(digits)

    return out

##############################

def get_tests():
    tests = []
    for x in range(1, get_int()):
        obj = get_object()
        tests.append(obj)
    return tests


def main():
    global depth
    depth = 0

    errDict = {}

    #Test each thing separately (all arrays, all nums, all strings, etc
    
    with open('fuzzInput.txt', 'a') as f:
        while True:
            #for testcase in get_tests():
            testcase = '''{"str":''' + get_string() + '''}'''
            #print testcase
            child = subprocess.Popen("./jsonParser", stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            _, stdErrOut = child.communicate(input = testcase)
            if child.returncode != 0 or stdErrOut != "":
                errMsg = stdErrOut.strip().split('\n')[0]
                #if errMsg not in errDict:
                    #errDict[errMsg] = testcase
                f.write(testcase + '\n')
                f.write(errMsg + '\n')
                print testcase
                print errMsg

            print
                    


if __name__ == '__main__':
    main()
