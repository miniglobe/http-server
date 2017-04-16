from http_request.file_exist_checker import check_exists
from http_response.file_reader import read
from http_response.response import add_header

def do_get(documentroot, wfile, path):
    if not _is_address(documentroot, wfile, path):
        if check_exists(documentroot, path):
            add_header(wfile,"200")
            read(documentroot, wfile, path)
        else:
            add_header(wfile,"404")


def _is_address(documentroot, wfile, path):

    if path == '/':
        add_header(wfile,"200")
        read(documentroot, wfile, '/index.html')
        return True
    else:
        return False
