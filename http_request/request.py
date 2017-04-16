import socketserver
from http_request.file_exist_checker import check_exists
from http_response.file_reader import read
from http_response.response import add_header

class MyRequestHandler(socketserver.StreamRequestHandler):

    def handle(self):
        data = self.rfile.readline().strip()
        print(data)
        method = data.decode('utf-8').split(' ')[0]
        path = data.decode('utf-8').split(' ')[1]
        if not self._is_address(path):
            if check_exists(self.documentroot, path):
                add_header(self.wfile,"200")
                read(self.wfile, self.documentroot, path)
            else:
                add_header(self.wfile,"404")


    def _is_address(self, path):

        if path == '/':
            add_header(self.wfile,"200")
            read(self.wfile, self.documentroot, '/index.html')
            return True
        else:
            return False
