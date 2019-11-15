# -*- coding: utf-8 -*-
__title__  = "payatuma"
__auther__ = "Furkan Sari and Ercan Sezdi"
__version__ = "0.2"
__email__  = "furkan210561@gmail.com and ercansezdizero@gmail.com"

import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib.patches as mpatches
from matplotlib.animation import FuncAnimation

class sinif():
    def __init__(self):
        print("Program Başladı!")
        #self.database()
        #self.dataekle()
        self.grafik()

    def grafik(self):
        self.x_data, self.y_data = [], []
        self.x_data2, self.y_data2 = [], []
        self.x_data3, self.y_data3 = [], []
        self.x_data4, self.y_data4 = [], []
        self.figure = plt.figure(figsize=(16, 8))
        plt.ylabel("kazanç")
        plt.xlabel("tarih")
        plt.title("Çizgi Dağılım");
        red_patch = mpatches.Patch(color='red', label='A101')
        green_patch = mpatches.Patch(color='green', label='ŞOK')
        blue_patch = mpatches.Patch(color='blue', label='BİM')
        black_patch = mpatches.Patch(color='black', label="HAPELOGLU")
        plt.legend(handles=[blue_patch, green_patch, red_patch, black_patch])
        self.xll = 0
        self.yll = 40
        #plt.ylim(0, 300)
        plt.xlim(self.xll, self.yll)
        self.ik = 1
        self.line, = plt.plot(self.x_data, self.y_data, color = 'red')
        self.line2,= plt.plot(self.x_data2, self.y_data2, color='green')
        self.line3, = plt.plot(self.x_data2, self.y_data2, color='blue')
        self.line4, = plt.plot(self.x_data2, self.y_data2, color='black')
        plt.grid()
        self.animation = FuncAnimation(self.figure, self.update, interval=200)
        plt.show()

    def update(self, frame):
        self.ik += 1
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

        self.x_data.append(self.ik)
        self.y_data.append(kisiler_name[self.ik])
        self.x_data2.append(self.ik)
        self.y_data2.append(kisiler_age[self.ik])
        self.x_data3.append(self.ik)
        self.y_data3.append(kisiler_uyruk[self.ik])
        self.x_data4.append(self.ik)
        self.y_data4.append(kisiler_cinsiyet[self.ik])
        self.line.set_data(self.x_data, self.y_data)
        self.line2.set_data(self.x_data2, self.y_data2)
        self.line3.set_data(self.x_data3, self.y_data3)
        self.line4.set_data(self.x_data4, self.y_data4)
        self.figure.gca().relim()
        self.figure.gca().autoscale_view()
        plt.xlim(self.xll, self.yll)
        if(self.ik >= 20):
            self.xll += 1
            self.yll += 1
        #return self.line,


    def dataekle(self):
        ax = 110
        bx = 100
        cx = 160
        vv=20
        with sqlite3.connect('vt.sqlite') as vt:
            im = vt.cursor()
            for i in range(250):
                a = random.randint(-20, 20)
                ax = ax + a
                b = random.randint(-20, 20)
                bx = bx + b
                c = random.randint(-20, 20)
                cx = cx + c
                d = random.randint(0, 5)
                vv = vv + d
                im.execute("""CREATE TABLE IF NOT EXISTS personel
                    (BİM, A101, ŞOK, HAPELOGLU)""")
                im.execute("""INSERT INTO personel VALUES
                    (?, ?, ?, ?)""", (ax, bx, cx , vv))
                vt.commit()

    def database(self):
        with sqlite3.connect("vt.sqlite") as vt:
            veriler = [('110', '120', '150', '0'),
                       ('120', '140', '170', '5'),
                       ('130', '120', '150', '10'),
                       ('110', '100', '160', '15')]
            im = vt.cursor()
            im.execute("""CREATE TABLE IF NOT EXISTS
                personel (BİM, A101, ŞOK, HAPELOGLU)""")

            for veri in veriler:
                im.execute("""INSERT INTO personel VALUES
                    (?, ?, ?, ?)""", veri)
            vt.commit()


if __name__ == "__main__":
    program = sinif()
