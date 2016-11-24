#!/usr/bin/env python3

from singleton import Singleton
from threading import Lock, Thread
import socket
import ssl
import struct


class Comm(Thread, metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self.listener = None
        self.lock = Lock()
        self.start()

    def run(self):
        self.__connect()
        while True:
            message = self.__receive()
            if message is None:
                break
            else:
                self.__dispatch(message)

    def __dispatch(self, message):
        with self.lock:
            if self.listener:
                self.listener(message)

    def set_listener(self, listener):
        with self.lock:
            self.listener = listener

    def __connect(self):
        self.context = ssl.create_default_context()
        self.context.load_verify_locations('../certs/server.crt')
        # Hard-coded for localhost, because this is an exercise.
        self.connection = self.context.wrap_socket(
                socket.socket(socket.AF_INET),
                server_hostname='localhost')
        self.connection.connect(('localhost', 2121))

    def disconnect(self):
        self.connection.shutdown(socket.SHUT_RDWR)
        self.connection.close()

    def send(self, message):
        data = message.encode('utf-8')
        data_len = struct.pack('>i', len(data))
        self.connection.send(data_len + data)

    def __receive(self):
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
            try:
                new_data = self.connection.recv(count - c)
            except Exception:
                return None
            if len(new_data) == 0:
                return None
            data += new_data
            c += len(new_data)
        return data
