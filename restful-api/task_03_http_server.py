import http.server
import socketserver
import json

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Əsas səhifə (Root)
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # Data endpoint-i (JSON qaytarır)
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))

        # Status endpoint-i
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # Info endpoint-i
        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode("utf-8"))

        # Tapılmayan endpoint-lər (404 Xətası)
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            # Testin gözlədiyi mətn: "Endpoint not found"
            self.wfile.write(b"Endpoint not found")

def run_server():
    PORT = 8000
    # Serveri quraşdırırıq
    with socketserver.TCPServer(("", PORT), SimpleAPIHandler) as httpd:
        print(f"Server {PORT} portunda işləyir...")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()
