import itertools


chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
wordlist = [p[0] + p[1] + p[2]  for p in itertools.product(chars, repeat=3)]
start = 'EECS388-'

for w in wordlist:
    print start + w
