# -*- coding: utf-8 -*-
__title__ = "binary_system"
__author__ = "Furkan Sarı and Ercan Sezdi"
__version__ = "0.0.2"
__email__ = "furkansari@mavirane.com and ercansezdizero@gmail.com"

from math import pow
from matplotlib import pyplot
import numpy as np


class program:
    def __init__(self):
        # Loop
        self.count = int(input('How many loops?\n'))
        self.stage = 1
        self.people_count = 1
        self.company_income = 0
        self.company_all_income = 0
        # Plot
        self.y_datas = []
        self.figure = pyplot.figure(figsize=(16, 8))
        self.loop = 1
        # Start Program
        self.start()
        self.plot()

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

    def plot(self):
        x = np.arange(0, self.count, 1)
        y = self.y_datas
        pyplot.plot(x, y, color='red')
        start_plot = pyplot.show()


if __name__ == "__main__":
    start = program()
