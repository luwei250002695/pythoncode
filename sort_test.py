#!/usr/bin/python
# -*- coding: utf-8 -*-

# Filename : sort_test.py
# author by : edgar
import random
b = [2, 3, 5, 6, 8, 9, 8, 8, 55, 8, 55, 11, 44, 55, 2, 3, 6, 5, 8, 9, 8, 7]
a = [x for x in range(1, 110)]   #生成列表,整数有序
print(a)
random.shuffle(a)                #洗牌
print(a)
def bubble_sort(alist):
    n = len(alist)
    print(n)
    for x in range(0, n-1):
        for i in range(0, n-1-x):
            if alist[i] > alist[i+1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
    return alist

bubble_sort(a)
print(a)
for x in range(0, 9):
    print(x, end=',')