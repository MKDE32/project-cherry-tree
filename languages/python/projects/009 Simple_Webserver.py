from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 80

server = HTTPServer(("0.0.0.0", PORT),SimpleHTTPRequestHandler)
print(f"Server läuft auf http://localhost:{PORT}")

server.serve_forever()
