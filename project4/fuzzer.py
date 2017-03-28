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

def get_int():
    return random.randint(0,10)
def get_chars():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(get_int()))

# get a tuple of shit
def get_tuple():
    return '\"' + get_chars() + '\":' + get_value()


def get_number():
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', 'e', 'E', '+', '-']
    return ''.join([random.choice(nums) for _ in range(0, random.randint(0, 10))])


def get_string():
    fukd = ['\\','\"','\\\\','\/','\b','\f','\r','\t','\u','\u12fd','\uzxdg3'] # ,'\n'
    temp = '\"'
    temp += ''.join([random.choice(fukd) for _ in range(0, random.randint(0, 10))])
    temp += get_chars()
    temp += '\"'
    return temp


# get json array
def get_list():
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
            list += get_obj()
        elif rand == 3:
            list += get_list()
        if i != 3:
            list += ','
    list += ']'

    dec_depth()
    return list



# get json object
def get_obj():
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


# return a list of tests
def get_tests():
    tests = []
    for x in range(1, get_int()):
        obj = get_obj()
        tests.append(obj)
    return tests

def get_true():
    return random.choice(['true', 'True', 'TRUE', 't', 'T', '1'])

def get_false():
    return random.choice(['false', 'False', 'FALSE', 'f', 'F', '0'])

def get_null():
    return random.choice(['null', 'Null', 'NULL'])

def get_value():
    return random.choice([get_string, get_number, get_obj, get_list, get_true, get_false, get_null])()

def main():
    global depth
    depth = 0
    
    while True:
    # for testcase in tests:
        broken = []
        tests = get_tests()
        for t in tests:
            print('START OF OBJ')
            print(t)
            print('END OF OBJ')
        for testcase in tests:
            child = subprocess.Popen("./jsonParser", stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            _, stdErrOut = child.communicate(input = testcase)
            if child.returncode != 0 or stdErrOut != "":
                broken.append(testcase)
                sys.exit(0)
        if len(broken) > 0:
            print(broken)
        break



if __name__ == '__main__':
    main()
