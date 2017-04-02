import socketserver
import threading

class MyRequestHandler(socketserver.StreamRequestHandler):

    def handle(self):
        data = self.rfile.readline().strip()
        print(data)

        self.wfile.write(b'HTTP/1.1 200 ok')
        self.wfile.write(b'\n')
        self.wfile.write(b'\n')
        self.wfile.write(b'<h1>hello</h1>')

def stop():
    command = input()
    if command == 'stop':
        server.shutdown()
        server_thread.join()
    else:
        stop()




if __name__ == "__main__":
    HOST, PORT = "192.168.33.10", 7777
    socketserver.TCPServer.allow_reuse_address = True

    server = socketserver.TCPServer((HOST, PORT), MyRequestHandler)

    ip, port = server.server_address
    print("IP: %s" % ip)
    print("Port: %s" % port)

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    stop()
