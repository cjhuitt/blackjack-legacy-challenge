#!/usr/bin/env python3

from singleton import Singleton
import socket
import ssl
import struct


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

    def send(self, message):
        if self.socket is None:
            return
        data = message.encode('utf-8')
        data_len = struct.pack('>i', len(data))
        self.socket.send(data + data_len)

    def receive(self):
        if self.socket is None:
            return None
        length_data = self.__receive_bytes(4)
        if length_data is None:
            return None
        length = struct.unpack('>i', length_data)[0]
        data = self.__receive_bytes(length)
        if data is None:
            return None
        return data.decode('utf-8')

    def __receive_bytes(self, count):
        c = 0
        data = b''
        while c < count:
            new_data = self.socket.recv(count - c)
            if len(new_data) == 0:
                self.socket = None
                return None
            data += new_data
            c += len(new_data)
        return data
