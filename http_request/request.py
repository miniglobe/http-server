import socketserver
from http_request.file_exist_checker import check_exists
from http_request.get import do_get
from http_response.file_reader import read
from http_response.response import add_header

class MyRequestHandler(socketserver.StreamRequestHandler):

    def handle(self):
        data = self.rfile.readline().strip()
        method = data.decode('utf-8').split(' ')[0]
        path = data.decode('utf-8').split(' ')[1]
        if method == 'GET':
            do_get(self.documentroot, self.wfile, path)
        elif method == 'POST':
            do_post(self.documentroot, self.wfile, path)
        else:
            print(b'other')
