# -*- coding: utf-8 -*-
__title__ = "binary_system"
__author__ = "Furkan Sarı and Ercan Sezdi"
__version__ = "0.0.3"
__email__ = "furkansari@mavirane.com and ercansezdizero@gmail.com"

from math import pow
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
import os


class program:
    def __init__(self):
        # Loop
        self.count = int(input('How many loops?\n'))
        self.y_datas = []
        self.stage = 1
        self.people_count = 1
        self.company_income = 0
        self.company_all_income = 0
        # Start Program
        self.start()
        # Plot
        self.loop = 0
        self.x_data, self.y_data = [], []
        self.figure = pyplot.figure(figsize=(16, 8))
        pyplot.xlim(0, 20)
        pyplot.ylim(0, 1000000)
        self.line, = pyplot.plot(self.x_data, self.y_data, '-')
        self.animation = FuncAnimation(self.figure, self.update, interval=200)
        pyplot.show()

    def start(self):
        for i in range(self.count):
            self.company_income = int(1000 * int(pow(2, (self.stage - 1))))
            self.company_all_income = self.company_income + self.company_all_income
            print('Stage ', self.stage, ' People Count:', self.people_count, ' Income: ', self.company_income)
            print('All Income: ', self.company_all_income)
            # New Stage
            self.stage += 1
            self.people_count *= 2
            self.y_datas.append(self.company_income)

    def update(self, frame):
        if self.loop == self.count:
            os.system('PAUSE')
        print(self.loop)
        print(self.y_datas)
        variable = self.y_datas[self.loop]
        self.x_data.append(self.loop)
        self.y_data.append(variable)
        self.line.set_data(self.x_data, self.y_data)
        self.figure.gca().relim()
        self.figure.gca().autoscale_view()
        self.loop += 1
        return self.line,


if __name__ == "__main__":
    start = program()
