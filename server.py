import http.server
import socketserver
import socket

PORT = 8000

# Define the handler to serve files from the current directory
Handler = http.server.SimpleHTTPRequestHandler

# Bind the server to all interfaces by using "0.0.0.0"
with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"Serving at http://{local_ip}:{PORT}")
    httpd.serve_forever()
