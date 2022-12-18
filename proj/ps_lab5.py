#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

EPS = 1e-10
if __name__ == '__main__':
    x = float(input("Input x: "))
    n = float(input("Input n: "))
    a = x
    s = 0
    k = 0
    while math.fabs(a) > EPS:
        a *= (((x ** 2) / 4) * (k + 1)) / ((k + 1) * (k + n))
        s = s + a
        k = k + 1
    print(f"I({x}) = {((x / 2)**2) * s}")


