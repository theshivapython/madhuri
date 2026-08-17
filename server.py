import http.server
import socketserver
import os
import sys

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

if __name__ == '__main__':
    os.chdir(DIRECTORY)
    if sys.stdout.encoding.lower() != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving Katari Madhuri's Cinematic Surprise at http://localhost:{PORT}")
        print(f"Access from mobile device on local Wi-Fi!")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped gracefully.")
            sys.exit(0)
