from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')


HOSTNAME = "localhost"
PORT = 8000
httpd = HTTPServer((HOSTNAME, PORT), SimpleHTTPRequestHandler)
print("Server starting at http://" + HOSTNAME + ":" + str(PORT))
httpd.serve_forever()
