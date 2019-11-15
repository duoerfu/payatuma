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
    def cheater_data(self,level,max = 32):
        gain = 0
        pwm = 0

        for i in range(0,level):
            gain += (2 ** i) * 1000

            print("Gün {} :".format(i + 1))
            if i == 0:
                print("Toplam Kazanç : {}".format(gain))
            else:
                pwm += 2 ** (i - 1)
                print("Toplam Kazanç : {}".format(gain - pwm * 120))



