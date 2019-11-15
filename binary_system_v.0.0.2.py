# -*- coding: utf-8 -*-
__title__ = "binary_system"
__author__ = "Furkan Sari and Ercan Sezdi"
__version__ = "0.0.1"
__email__ = "furkansari@mavirane.com and ercansezdizero@gmail.com"

from math import pow


class program:
    def __init__(self):
        print("Program Start!")
        self.increase = 5
        self.day = 3
        self.stage = 3
        self.people_count = 2
        self.all_people = 3
        self.company_all_income = 3000
        self.start()

    def start(self):
        for i in range(7):
            self.company_income = int(1000 * int(pow(2, (self.stage - 1))))
            print(self.day, ' gün', self.stage, ' stage')
            self.company_all_income = self.company_income + self.company_all_income
            print('Company Income', self.company_income)
            print('Company All Income = ', self.company_all_income)
            self.all_people = self.people_count + self.all_people
            self.people_count = int(pow(2, self.stage))
            print('How many people =', self.all_people)
            print('------------------------')
            self.day += self.increase
            self.increase *= 2
            self.stage += 1


if __name__ == "__main__":
    start = program()
