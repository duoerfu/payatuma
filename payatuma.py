#!/usr/bin/env python

__author__ = "Ercan Sezdi & Furkan Sarı"
__version__ = 0.1


from random import randint

class payatuma:
    def __init__(self):
        self.name = "Ercan"

    def random_veri(self,limit,data = 0):
        if limit != 0:
            if data - limit < 0:
                return 0
            else:
                return randint(data - limit , data + limit)
        else:
            return randint(0,500)
