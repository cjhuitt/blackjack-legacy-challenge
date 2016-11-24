#!/usr/bin/env python3

from singleton import Singleton

class User(metaclass=Singleton):
    def __init__(self):
        self.name = ''
        self.money = 0
