#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Поле first — дробное число; поле second — дробное число,
показатель степени. Реализовать метод power() — возведение числа
first в c тепень second. Метод должен правильно работать при любых
допустимых значениях first и second.
"""


class Myclass:

    def __init__(self, first=0, second=0):
        self.first = float(first)
        self.second = float(second)

    def read(self):
        first = input('Введите дробное число: ')
        second = input('Введите целое число, показатель степени: ')

        self.first = float(first)
        self.second = float(second)

    def display(self):
        print("Вы хотите получить число {0} в "
              "степени {1}".format(self.first, self.second))

    def make_power(self):
        if self.first == 0:
            raise ValueError()
        else:
            k = self.first ** self.second
            print("Ответ - ", k)


if __name__ == '__main__':
    test = Myclass()
    test.read()
    test.display()
    test.make_power()
