# -*- coding: utf-8 -*-
__title__ = "binary_system"
__author__ = "Furkan Sari and Ercan Sezdi"
__version__ = "0.0.1"
__email__ = "furkansari@mavirane.com and ercansezdizero@gmail.com"

from math import pow


class program:
    def __init__(self):
        print("Program Start!")
        self.day = 3
        self.start()

    def start(self):
        print(self.day, ' gün')


if __name__ == "__main__":
    start = program()
