#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = float(input("Введите коэф а: "))
    b = float(input("Введите коэф b: "))
    c = float(input("Введите коэф c: "))
    if a != 0:
        d = b**2 - 4 * a * c
        if d == 0:
            t = -b / (2 * a)
            x1 = t ** 0.5
            x2 = - (t ** 0.5)
            print(x1, x2)
        elif d > 0:
            t1 = (-b + d ** 0.5) / (2 * a)
            t2 = (-b - d ** 0.5) / (2 * a)
            x3 = t1 ** 0.5
            x4 = - (t1 ** 0.5)
            x5 = t2 ** 0.5
            x6 = - (t2 ** 0.5)
            print("Корни: ", x3, x4, x5, x6)
        elif d < 0:
            print("Корней нет")
    else:
        print("а не должно = 0")