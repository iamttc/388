#!/user/bin/bash/python

import subprocess
import os
import base64
import sys
import random
import string

def get_int():
    return random.randint(0,50)
def get_string():
    temp = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(get_int()))
    return '\"' + temp + '\"'


# get a tuple of shit
def get_tuple():
    
    tp = get_string() + ':'

    i = random.randint(1, 10)
    x = random.randint(1, 10)

    if x % i == 0: # integer
        tp += str(get_int())

    else: # string
        tp += get_string()

    return str(tp)



# get json object
def get_obj():
    obj = '{'
    for x in range(get_int()):
        obj += get_tuple()
        obj += ','
    obj += '}'
    return obj


# return a list of tests
def get_tests():
    tests = []
    for x in range(1, get_int()):
        obj = get_obj()
        tests.append(obj)
    return tests

def get_number():
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', 'e', 'E', '+', '-']
    return ''.join([random.choice(nums) for _ in range(0, random.randint(0, 50))])

def get_true():
    return random.choice(['true', 'True', 'TRUE', 't', 'T', '1'])

def get_false():
    return random.choice(['false', 'False', 'FALSE', 'f', 'F', '0']

def get_null():
    return random.choice(['null', 'Null', 'NULL'])

def get_value():
    return random.choice([get_string, get_number, get_obj, get_list, get_true, get_false, get_null])()

def main():
    
    while True:
    # for testcase in tests:
        broken = []
        tests = get_tests()
        for testcase in tests:
            child = subprocess.Popen("./jsonParser", stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            _, stdErrOut = child.communicate(input = testcase)
            if child.returncode != 0 or stdErrOut != "":
                broken.append(testcase)
                sys.exit(0)



if __name__ == '__main__':
    main()
