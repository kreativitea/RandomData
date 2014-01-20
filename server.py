#!/usr/bin/env python 

import socket
import pprint

import settings


def serve():
    ''' A simple echo server to use in test. '''
    host = '127.0.0.1'
    port = int(settings.PORT)
    backlog = 5
    size = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(backlog)
    while 1:
        client, address = s.accept()
        data = client.recv(size)
        if data:
            client.send(data)
            print data
        client.close()

if __name__ == "__main__":
    serve()