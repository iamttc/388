import hashlib
import itertools

def get_hash():
    start = '27204f52203123'
    counter = 0

    while 1:
        password = str(counter)
        passhash = hashlib.md5(password).hexdigest()

        if start == passhash[:14]:
            print password
            print passhash
            print passhash.decode('hex')
            return

        counter += 1

get_hash()

