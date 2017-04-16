def add_header(wfile,status):
    import time

    t = time.strftime('%a, %d %b %Y %X')
    t = str(t)
    if status == "200":
        wfile.write(b'HTTP/1.1 200 OK')
    if status == "404":
        wfile.write(b'HTTP/1.1 404 Not Found')

    wfile.write(b'HTTP/1.1')
    wfile.write(b'\n')
    wfile.write(b'Date: ' + t.encode('utf-8'))
    wfile.write(b'\n')
    wfile.write(b'Server: Guroche/0.3.22 (Unix) (Ubuntu/Linux)')
    wfile.write(b'\n')
    wfile.write(b'Last-Modified:')
    wfile.write(b'\n')
    wfile.write(b'ETag:')
    wfile.write(b'\n')
    wfile.write(b'Accept-Ranges:')
    wfile.write(b'\n')
    wfile.write(b'Content-Length:')
    wfile.write(b'\n')
    wfile.write(b'keep-Alive: timeout=xx, max=yy')
    wfile.write(b'\n')
    wfile.write(b'Connection: Keep-Alive')
    wfile.write(b'\n')
    wfile.write(b'Content-Type: text/html')
    wfile.write(b'\n')
    wfile.write(b'\n')
