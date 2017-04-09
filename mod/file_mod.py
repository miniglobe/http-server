import os

def check_exists(documentroot,path):

    if os.path.isfile(documentroot + path):
        return True
    else:
        return False


def write(wfile, documentroot, path):

    with open(documentroot + path) as f:
        for line in f:
            line = f.readline()
            wfile.write(line.encode('utf-8'))
    return
