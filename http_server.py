import socketserver

class MyRequestHandler(socketserver.StreamRequestHandler):

    def handle(self):
        data = self.rfile.readline().strip()
        print(data)

        self.wfile.write(data)
        self.wfile.write(b'\n')


if __name__ == "__main__":
    HOST, PORT = "localhost", 7778

    server = socketserver.TCPServer((HOST, PORT), MyRequestHandler)

    ip, port = server.server_address
    print("IP: %s" % ip)
    print("Port: %s" % port)

    server.serve_forever()
