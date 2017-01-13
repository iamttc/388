from pymd5 import md5, padding
import httplib, urlparse, sys, urllib, math

#For now just playing around with length extension
#og_message = "Use HMAC, not hashes"
#og_hash = md5(og_message).hexdigest()
#print og_message
#print og_hash
#
#
#h = md5(state=og_hash.decode('hex'), count=512)
#x = "Good advice"
#h.update(x)
#
##Created using only the hash of the original message and a its length
#print h.hexdigest()
##Created using the original message itself
#print md5(og_message + padding(len(og_message)*8) + x).hexdigest()

#Get original url
#url = sys.argv[1]
url = 'https://eecs388.org/project1/api?token=402a574d265dc212ee64970f159575d0&user=admin&command1=ListFiles&command2=NoOp'
print(url)
parsedUrl = urlparse.urlparse(url)
token = parsedUrl.query.split('&')[0][6:]
message = parsedUrl.query.split('&', 1)[1]

#Conduct attack
extension = '&command3=UnlockAllSafes'
state = token.decode('hex')
length_of_m = 8 + len(message) #bytes
count = (length_of_m + len(padding(length_of_m * 8))) * 8 #bits

h = md5(state=state, count=count)
h.update(extension)
newtoken = urllib.quote(h.hexdigest())

url = 'https://' + parsedUrl.hostname + parsedUrl.path + '?token=' + newtoken + '&' + message + extension

#Send url
parsedUrl = urlparse.urlparse(url)
conn = httplib.HTTPSConnection(parsedUrl.hostname, parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()


