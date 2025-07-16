import http.server
import socketserver

PORT = 8080

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith(".css"):
            self.send_response(200)
            self.send_header("Content-type", "text/css")
            self.end_headers()
            with open(self.path[1:], 'rb') as file:
                self.wfile.write(file.read())
        elif self.path.endswith(".js"):
            self.send_response(200)
            self.send_header("Content-type", "application/javascript")
            self.end_headers()
            with open(self.path[1:], 'rb') as file:
                self.wfile.write(file.read())
        else:
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
