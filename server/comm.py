#!/usr/bin/env python3

from singleton import Singleton
import socket
import ssl


class Comm(metaclass=Singleton):
    def __init__(self):
        self.context = ssl.create_default_context()
        self.context.load_cert_chain(
                certfile='../certs/server.crt',
                keyfile='../certs/server.key')
        self.context.verify_mode = ssl.CERT_OPTIONAL
        self.context.check_hostname = False
        self.bindsocket = socket.socket()
        # Hard-coded for localhost, because this is an exercise.
        self.bindsocket.bind(('localhost', 2121))
        self.bindsocket.listen(0)
        self.socket = None

    def wait(self):
        if self.socket is not None:
            return
        socket, addr = self.bindsocket.accept()
        self.socket = self.context.wrap_socket(socket, server_side=True)
        print(self.socket.read().decode('utf-8'))
