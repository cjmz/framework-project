# 1. Create a basic HTTP server to handle requests and responses.
# 2. Implement routing to map URLs to specific handler functions.
# 3. Develop a controller to process incoming requests and return appropriate responses.
# 4. Create a model to interact with data storage (e.g., database).
# 5. Implement a view to render HTML templates and return them as responses.
# 6. Set up a configuration file to manage settings like server port, database connections, etc.
# 7. Add error handling to manage different HTTP status codes and exceptions.
# 8. Implement middleware for tasks like logging, authentication, and request parsing.
# 9. Write unit tests to ensure the framework components work correctly.
# 10. Document the framework with usage examples and API references.


# Ideias
# Criar um automatizador baseado no artisan do Laravel
# Criar migrations baseadas no migration do laravel e do Rails

from http.server import HTTPServer
from router.paths import Router


def run(server_class=HTTPServer, handler_class=Router):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('Server running on :8000')
    httpd.serve_forever()
    

run()