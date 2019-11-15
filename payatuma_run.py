#!/usr/bin/env python

__author__ = "Ercan Sezdi & Furkan Sarı"
__version__ = 0.1

import payatuma
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class draw_graph():
    def __init__(self,sirketSayisi = 5, uretilecekVeriSayisi = 250, artisLimit = 10):
        self.sirketSayisi = sirketSayisi
        self.uretilecekVeriSayisi = uretilecekVeriSayisi
        self.artisLimit = artisLimit
        self.data = payatuma.payatuma()
    def start(self):
        dataArray = []
        for counter in range(0, self.sirketSayisi):
            dataArray.append(self.data.random_veri(2, 50))
            counter += 1
        sayac = 0
        for i in dataArray:
            veri = i
            dataArrayCon = []
            for counter in range(0, self.uretilecekVeriSayisi):
                veri = self.data.random_veri(self.artisLimit, veri)
                dataArrayCon.append(veri)
            dataArray[sayac] = dataArrayCon
            sayac += 1

        #for i in range(0, len(dataArray)):
        #    print(dataArray[i])

        fig, ax = plt.subplots()
        for i in dataArray:
            ax.plot(i)
        ax.grid()
        plt.show()
    def test(self):
        self.data.cheater_data(10,32)

if __name__ == "__main__":
    start = draw_graph()
    start.test()



