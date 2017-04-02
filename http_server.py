import socketserver
import threading
import configparser
import os
import datetime
import time

class HttpServer(object):


    class MyRequestHandler(socketserver.StreamRequestHandler):

        def handle(self):
            data = self.rfile.readline().strip()
            path = data.decode('utf-8').split(' ')[1]
            if not self._is_address(path):
                self._check_file_exists(path)


        def _is_address(self, path):

            if path == '/':
                self._add_header()
                self._display_body()
                return True
            else:
                return False


        def _add_header(self):

            t = time.strftime('%a, %d %b %Y %X')
            t = str(t)
            self.wfile.write(b'HTTP/1.1 200 ok')
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


        def _display_body(self):

            with open(self.documentroot + '/index.html') as f:
                for line in f:
                    line = f.readline()
                    self.wfile.write(line.encode('utf-8'))
            return



        def _check_file_exists(self, path):

            if os.path.isfile(self.documentroot + path):
                self.wfile.write(b'HTTP/1.1 200 OK')
                self._add_header()
                with open(self.documentroot + path) as f:
                    for line in f:
                        line = f.readline()
                        self.wfile.write(line.encode('utf-8'))
            else:
                self.wfile.write(b'HTTP/1.1 404 Not Found')


    def __init__(self, documentroot, host, port):

        self.documentroot = documentroot
        socketserver.TCPServer.allow_reuse_address = True
        self.server = socketserver.TCPServer((host, port), self.MyRequestHandler)
        self.host = host
        self.port = port
        self.MyRequestHandler.documentroot = self.documentroot

    @property
    def server_address(self):

        return self.host, self.port


    def start(self):

        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()


    def stop(self):
        self.server.shutdown()
        self.server_thread.join()


def stop(server):

    command = input()
    if command == 'stop':
        server.stop()
    else:
        stop(server)

def load_config():

    config = configparser.ConfigParser()
    config.read('./config/config.ini')
    host = config['settings']['host']
    port = int(config['settings']['port'])
    documentroot = config['settings']['documentroot']
    return host, port, documentroot


if __name__ == "__main__":

    HOST, PORT, DOCUMENTROOT = load_config()
    server = HttpServer(DOCUMENTROOT, HOST, PORT)
    server.start()
    ip, port = server.server_address
    print("IP: %s" % ip)
    print("Port: %s" % port)
    stop(server)
