# -*- coding: utf-8 -*-
__title__ = "binary_system"
__author__ = "Furkan Sari and Ercan Sezdi"
__version__ = "0.0.1"
__email__ = "furkansari@mavirane.com and ercansezdizero@gmail.com"

from math import pow


class program:
    def __init__(self):
        print("Program Start!")
        self.gun = 1
        self.kademe = 1
        self.company_all_income = 0
        self.start()

    def start(self):
        for i in range(14):
            self.company_income = int(1000 * int(pow(2, (self.kademe - 1))))
            if self.kademe < 7:
                print(self.gun, ' gün', self.kademe, ' kademe')
                self.company_all_income = self.company_income + self.company_all_income
                print(self.company_all_income)
                self.gun += 1
                self.kademe += 1
            if 6 < self.kademe < 11:
                self.company_income = int(1000 * int(pow(2, (self.kademe - 1))))
                for j in range(32):
                    print(self.gun, ' gün', self.kademe, ' kademe')
                    print(self.company_income, 'company income')
                    self.company_all_income = int(int(self.company_income / 32) + int(self.company_all_income))
                    print(self.company_all_income)
                    self.gun += 1
                self.kademe += 1


if __name__ == "__main__":
    start = program()
