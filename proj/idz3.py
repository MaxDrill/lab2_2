#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    N = int(input("Vvedite razmer spiska: "))
    lst = [int(input("Vvedite chis: ")) for i in range(N)]
    for i in range(N):
        a = lst[i] % 10
        b = lst[i] // 10
        summ = a + b
        if lst[i] % summ == 0:
            a = 0
            b = 0
            print(lst[i], "delitsa")
        else:
            print(lst[i], "ne delitsa")

