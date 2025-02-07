import http.server
import random
import socketserver
import webbrowser
import threading


class Server:
    def __init__(self, port=None):
        self.routes = {}
        self.port = port or random.randint(49000, 49999)

    def start_server(self):
        handler = self.create_handler()
        with socketserver.TCPServer(("", self.port), handler) as httpd:
            httpd.allow_reuse_address = True  # Allow port reuse
            print(f"Serving at http://localhost:{self.port}/")
            httpd.serve_forever()

    def open_index(self):
        # Start server in a separate thread
        server_thread = threading.Thread(target=self.start_server)
        server_thread.daemon = True
        server_thread.start()

        webbrowser.open(f"http://localhost:{self.port}/")

        # Keep the main thread running
        input("Press Enter to stop the server...\n")

    def route(self, path):
        """Registers a route with a corresponding handler function.

        This method is a decorator that associates a given URL path with a 
        function that handles requests for that path. The function should 
        take path as an argument and return either a redirect dict or
        an HTML response as a string.

        Args:
            path (str): The URL path to associate with the handler function.

        Returns:
            function: A decorator that registers the function as the handler 
            for the specified route.

        Example:
            server = Server()

            @server.route("/hello")
            def hello():
                return "<h1>Hello, World!</h1>"

            @server.route("/old_hello")
            def old_hello():
                return {"redirect": "/hello"}
        """
        def decorator(fn):
            self.routes[path] = fn
            return fn
        return decorator

    def create_handler(self):
        routes = self.routes

        class DynamicHandler(http.server.BaseHTTPRequestHandler):
            def do_GET(self):
                view_fn = routes.get(self.path, routes.get("default", None))
                if view_fn:
                    return self.send_or_redirect(view_fn(self.path))
                return self.send_404()

            def send_or_redirect(self, content):
                if isinstance(content, dict) and "redirect" in content:
                    target_url = content["redirect"]
                    self.send_response(302)
                    self.send_header("Location", target_url)
                    self.end_headers()
                elif isinstance(content, str):
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(content.encode("utf-8"))
                else:
                    self.send_404()

            def send_404(self):
                self.send_response(404)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"<html><body><h1>404 Not Found</h1></body></html>")

        return DynamicHandler
