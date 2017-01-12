from pymd5 import md5, padding

#For now just playing around with length extension
og_message = "Use HMAC, not hashes"
og_hash = md5(og_message).hexdigest()
print og_message
print og_hash


h = md5(state=og_hash.decode('hex'), count=512)
x = "Good advice"
h.update(x)

#Created using only the hash of the original message and a its length
print h.hexdigest()
#Created using the original message itself
print md5(og_message + padding(len(og_message)*8) + x).hexdigest()
