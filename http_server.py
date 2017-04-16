import socketserver
import threading
import configparser
import os
import datetime
import time

from http_request.request import MyRequestHandler

class HttpServer(object):

    def __init__(self, documentroot, host, port):

        self.documentroot = documentroot
        socketserver.TCPServer.allow_reuse_address = True
        self.server = socketserver.TCPServer((host, port), MyRequestHandler)
        self.host = host
        self.port = port
        MyRequestHandler.documentroot = self.documentroot

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
