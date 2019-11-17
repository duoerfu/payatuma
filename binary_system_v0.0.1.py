# -*- coding: utf-8 -*-
__title__ = "binary_system"
__author__ = "Furkan Sari and Ercan Sezdi"
__version__ = "0.0.1"
__email__ = "furkansari@mavirane.com and ercansezdizero@gmail.com"

from math import pow


class program:
    def __init__(self):
        self.stage = 1
        self.people_count = 1
        self.company_income = 0
        self.company_all_income = 0
        # Start Program
        self.start()

    def start(self):
        count = int(input('How many loops?\n'))
        for i in range(count):
            self.company_income = int(1000 * int(pow(2, (self.stage - 1))))
            self.company_all_income = self.company_income + self.company_all_income
            print('Stage ', self.stage, ' People Count:', self.people_count, ' Income: ', self.company_income)
            print('All Income: ', self.company_all_income)
            # New Stage
            self.stage += 1
            self.people_count *= 2


if __name__ == "__main__":
    start = program()
