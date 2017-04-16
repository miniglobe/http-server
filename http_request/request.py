import socketserver
import time
from http_request.file_exist_checker import check_exists
from http_response.file_reader import read

class MyRequestHandler(socketserver.StreamRequestHandler):

    def handle(self):
        data = self.rfile.readline().strip()
        method = data.decode('utf-8').split(' ')[0]
        path = data.decode('utf-8').split(' ')[1]
        if not self._is_address(path):
            if check_exists(self.documentroot, path):
                self._add_header("200")
                read(self.wfile, self.documentroot, path)
            else:
                self._add_header("404")


    def _is_address(self, path):

        if path == '/':
            self._add_header("200")
            read(self.wfile, self.documentroot, '/index.html')
            return True
        else:
            return False


    def _add_header(self, status):

        t = time.strftime('%a, %d %b %Y %X')
        t = str(t)
        if status == "200":
            self.wfile.write(b'HTTP/1.1 200 OK')
        if status == "404":
            self.wfile.write(b'HTTP/1.1 404 Not Found')

        self.wfile.write(b'HTTP/1.1')
        self.wfile.write(b'\n')
        self.wfile.write(b'Date: ' + t.encode('utf-8'))
        self.wfile.write(b'\n')
        self.wfile.write(b'Server: Guroche/0.3.22 (Unix) (Ubuntu/Linux)')
        self.wfile.write(b'\n')
        self.wfile.write(b'Last-Modified:')
        self.wfile.write(b'\n')
        self.wfile.write(b'ETag:')
        self.wfile.write(b'\n')
        self.wfile.write(b'Accept-Ranges:')
        self.wfile.write(b'\n')
        self.wfile.write(b'Content-Length:')
        self.wfile.write(b'\n')
        self.wfile.write(b'keep-Alive: timeout=xx, max=yy')
        self.wfile.write(b'\n')
        self.wfile.write(b'Connection: Keep-Alive')
        self.wfile.write(b'\n')
        self.wfile.write(b'Content-Type: text/html')
        self.wfile.write(b'\n')
        self.wfile.write(b'\n')
