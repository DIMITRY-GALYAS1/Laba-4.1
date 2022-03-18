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
        print("Ответ - ", make_power(self.first, self.second))


def make_power(first, second):
    if first == 0:
        raise ValueError()
    else:
        k = first ** second
        return k


if __name__ == '__main__':
    test = Myclass()
    test.read()
    test.display()
