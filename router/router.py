from http.server import SimpleHTTPRequestHandler

class Router(SimpleHTTPRequestHandler):
    routes = {}

    @classmethod

    def add_route(cls, path, handler):
        cls.routes[path] = handler

    def do_GET(self):
        handler = self.routes.get(self.path)

        if handler:
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            handler(self)
        else:
           self.send_response(404)
           self.end_headers()
           self.wfile.write(b'404 Not Found')

