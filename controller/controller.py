class Controller:
    @staticmethod
    def render_view(request, view_name):
        try:
            with open('views/' + view_name, 'r') as file:
                content = file.read()
            request.wfile.write(content.enconde())
        except FileNotFoundError:
            request.send_response(404)
            request.end_headers()
            request.wfile.write(b'Not found!')