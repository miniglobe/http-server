def read(documentroot, wfile, path):

    with open(documentroot + path) as f:
        for line in f:
            line = f.readline()
            wfile.write(line.encode('utf-8'))
    return
