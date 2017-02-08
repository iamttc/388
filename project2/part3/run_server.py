import BaseHTTPServer, SimpleHTTPServer
import ssl

class CORSRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def end_headers(self):
		self.send_header('Access-Control-Allow-Origin','*')
		SimpleHTTPServer.SimpleHTTPRequestHandler.end_headers(self)

httpd = BaseHTTPServer.HTTPServer(('localhost', 31337), CORSRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='server.pem', server_side=True)
httpd.serve_forever()
