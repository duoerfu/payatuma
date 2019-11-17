# -*- coding: utf-8 -*-
__title__  = "payatuma"
__auther__ = "Furkan Sari and Ercan Sezdi"
__version__ = "0.1"
__email__  = "furkan210561@gmail.com and ercansezdizero@gmail.com"

import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib.patches as mpatches

class sinif():
    def __init__(self):
        print("Program Başladı!")
        #self.dataekle()
        #self.database()
        self.grafik()

    def dataekle(self):
        vv=0
        with sqlite3.connect('vt.sqlite') as vt:
            im = vt.cursor()
            for i in range(60):
                a = random.randint(100, 300)
                b = random.randint(100, 300)
                c = random.randint(100, 300)
                d = random.randint(0, 15)
                vv = vv + d
                im.execute("""CREATE TABLE IF NOT EXISTS personel
                    (BİM, A101, ŞOK, HAPELOGLU)""")
                im.execute("""INSERT INTO personel VALUES
                    (?, ?, ?, ?)""", (a, b, c , vv))
                vt.commit()

    def grafik(self):
        kisiler_name = []
        kisiler_age = []
        kisiler_uyruk = []
        kisiler_cinsiyet = []
        with sqlite3.connect('vt.sqlite') as vt:
            im = vt.cursor()
            im.execute("""SELECT * FROM personel""")
            veriler = im.fetchall()
            uzunluk = int(len(veriler))
            for i in range(uzunluk):
                im.execute("""SELECT * FROM personel""")
                kisiler_name.append(int(im.fetchall()[i][0]))
                im.execute("""SELECT * FROM personel""")
                kisiler_age.append(int(im.fetchall()[i][1]))
                im.execute("""SELECT * FROM personel""")
                kisiler_uyruk.append(int(im.fetchall()[i][2]))
                im.execute("""SELECT * FROM personel""")
                kisiler_cinsiyet.append(int(im.fetchall()[i][3]))

        x = np.arange(0,uzunluk,1)
        y = kisiler_name
        plt.figure(figsize=(16, 8))
        plt.xlim(0, 100)
        plt.ylim(0,450)
        #plt.subplot(2, 2, 1)
        plt.plot(x, y, color='red')#, '-ob')
        plt.ylabel("kazanç")
        plt.xlabel("tarih")
        plt.title("Çizgi Dağılım");
        x = np.arange(0,uzunluk,1)
        y = kisiler_age
        plt.plot(x, y, color='green')
        x = np.arange(0, uzunluk, 1)
        y = kisiler_uyruk
        plt.plot(x, y, color='blue')
        plt.grid()
        y = kisiler_cinsiyet
        plt.plot(x, y, color='black')
        plt.grid()

        red_patch = mpatches.Patch(color='red', label='A101')
        green_patch = mpatches.Patch(color='green', label='ŞOK')
        blue_patch = mpatches.Patch(color='blue', label='BİM')
        black_patch = mpatches.Patch(color='black', label="HAPELOGLU")
        plt.legend(handles=[blue_patch,green_patch,red_patch,black_patch])

        a = plt.show()


    def database(self):
        with sqlite3.connect("vt.sqlite") as vt:
            veriler = [('110', '120', '150', '0'),
                       ('200', '130', '120', '50'),
                       ('150', '140', '110', '100'),
                       ('170', '170', '94', '200')]
            im = vt.cursor()
            im.execute("""CREATE TABLE IF NOT EXISTS
                personel (BİM, A101, ŞOK, HAPELOGLU)""")

            for veri in veriler:
                im.execute("""INSERT INTO personel VALUES
                    (?, ?, ?, ?)""", veri)
            vt.commit()


if __name__ == "__main__":
    program = sinif()
