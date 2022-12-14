#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    for i in range(10, 100):
        a = i % 10
        b = i // 10
        summ = a + b
        if i % summ == 0:
            a = 0
            b = 0
            print(i, "delitsa")

