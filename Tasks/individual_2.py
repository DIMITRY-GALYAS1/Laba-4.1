#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать класс ModelWindow для работы с моделями экранных окон. В качестве полей
задаются: заголовок окна, координаты левого верхнего угла, размер по
горизонтали, размер по вертикали, цвет окна, состояние «видимое/невидимое»,
состояние «с рамкой/без рамки». Координаты и размеры указываются в целых
числах. Реализовать операции: передвижение окна по горизонтали,по вертикали;
изменение высоты и/или ширины окна изменение цвета; изменение состояния,
опрос состояния. Операции передвижения и изменения размера должны осуществлять
проверку на пересечение границ экрана. Функция вывода на экран должна и
ндуцировать состояние полей объекта.
"""


class ModelWindow:

    def __init__(self, zagolovok, x, y, gorizontal, vertical, color, condition, frame_status):
        self.zagolovok = str(zagolovok)
        self.x = int(x)
        self.y = int(y)
        self.gorizontal = int(gorizontal)
        self.vertical = int(vertical)
        self.color = str(color).lower()
        self.condition = str(condition).lower()
        self.frame_status = str(frame_status).lower()

    def read(self):
        zagolovok = input("Введите заголовок: ")

        self.zagolovok = str(zagolovok)

    def change_width_and_height(self):
        new_width = int(input("Введите новую ширину: "))
        new_height = int(input("Введите новую высоту: "))

        if new_width > 1920 or new_height > 1080:
            raise ValueError()
        else:
            self.gorizontal = new_width
            self.vertical = new_height

    def peremeshenie(self):
        # Расчет допустимого перемещения по x вправо
        right_x = 1080 - (self.x + self.gorizontal)
        # Расчет допустимого перемещения по x влево
        left_x = self.x
        # Расчет допустимого перемещения по y вверх
        top_y = 1920 - self.y
        # Расчет допустимого перемещения по y вниз
        bottom_y = self.y - self.vertical

        k = int(input("Переместить влево - 1, вправо - 2, "
                      "вниз - 3, вверх - 4: "))
        b = int(input("Насколько переместить? "))

        if k == 1:
            if left_x < b:
                raise ValueError()
            else:
                self.x = self.x - b
        elif k == 2:
            if right_x < b:
                raise ValueError()
            else:
                self.x = self.x + b
        elif k == 3:
            if bottom_y < b:
                raise ValueError()
            else:
                self.y = self.y - b
        elif k == 4:
            if top_y < b:
                raise ValueError()
            else:
                self.y = self.y + b

        return self.x, self.y

    def display(self):
        print("\nНовые параметры окна \n")
        print(f"Заголовок окна: {self.zagolovok}")
        print(f"Ширина окна: {self.gorizontal} а высота окна: {self.vertical}")
        print(f"Координаты  окна по x {self.x} а по y {self.y}")
        print(f"Цвет окна: {self.color}")
        print(f"Видимость рамки: {self.condition}")
        print(f"Состояние с рамкой/без рамки: {self.frame_status} \n")

    def change_color(self):
        z_color = str(input("Введите новый цвет: ")).lower()
        if self.color != z_color:
            self.color = z_color

    def change_condition(self):
        z_condition = str(input("Введите состояние окна: ")).lower()
        z_frame_status = str(input("Введите состояние рамки: ")).lower()

        if self.condition != z_condition:
            self.condition = z_condition
        if self.frame_status != z_frame_status:
            self.frame_status = z_frame_status


if __name__ == '__main__':
    r1 = ModelWindow("Окно", 0, 0, 0, 0, "Черный", "Видимая", "С рамкой")
    r1.read()
    r1.display()
    r1.change_width_and_height()
    r1.display()
    r1.peremeshenie()
    r1.display()
    r1.change_color()
    r1.display()
    r1.change_condition()
    r1.display()
