#!/usr/bin/env python

__author__ = "Ercan Sezdi & Furkan Sarı"
__version__ = 0.1

import payatuma
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    data = payatuma.payatuma()
    sirketSayisi = 5
    uretilecekVeriSayisi = 250
    artisLimit = 10



    dataArray = []
    for counter in range(0,sirketSayisi):
        dataArray.append(data.random_veri(2,50))
        counter += 1
    sayac = 0
    for i in dataArray:
        veri = i
        dataArrayCon = []
        for counter in range(0,uretilecekVeriSayisi):
            veri = data.random_veri(artisLimit, veri)
            dataArrayCon.append(veri)
        dataArray[sayac] = dataArrayCon
        sayac += 1

    for i in range(0,len(dataArray)):
        print(dataArray[i])

    fig, ax = plt.subplots()
    for i in dataArray:
        ax.plot(i)
    ax.grid()
    plt.show()
