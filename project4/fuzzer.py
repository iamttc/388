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
    return random.choice(['true', 'True', 'TRUE', 't', 'T', '1'])

def get_false():
    return random.choice(['false', 'False', 'FALSE', 'f', 'F', '0'])

def get_null():
    return random.choice(['null', 'Null', 'NULL'])

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

    list = '['
    for i in range(0,4):
        rand = random.randint(0,4)
        if rand == 0:
            list += get_number()
        elif rand == 1:
            list += get_string()
        elif rand == 2:
            list += get_object()
        elif rand == 3:
            list += get_array()
        if i != 3:
            list += ','
    list += ']'

    dec_depth()
    return list

def get_value():
    return random.choice([get_string, get_number, get_object, get_array, get_true, get_false, get_null])()

def get_string():
    fukd = ['\\','\"','\\\\','\/','\b','\u','\u12fd','\uzxdg3'] # ,'\n', '\r', '\t', '\f'
    temp = '\"'
    temp += ''.join([random.choice(fukd) for _ in range(0, random.randint(0, 10))])
    temp += get_chars()
    temp += '\"'
    return temp

def get_number():
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', 'e', 'E', '+', '-']
    return ''.join([random.choice(nums) for _ in range(0, random.randint(0, 10))])

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
    
    with open('fuzzInput.txt', 'a') as f:
        while True:
            for testcase in get_tests():
                child = subprocess.Popen("./jsonParser", stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                _, stdErrOut = child.communicate(input = testcase)
                if child.returncode != 0 or stdErrOut != "":
                    errMsg = stdErrOut.strip().split('\n')[0]
                    if errMsg not in errDict:
                        errDict[errMsg] = testcase
                        f.write(errMsg + '\n')
                        f.write(testcase + '\n')
                        print errMsg
                    


if __name__ == '__main__':
    main()
