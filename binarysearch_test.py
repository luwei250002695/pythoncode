#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random

import numpy as np


def binarysearch(array, m):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        midval = array[mid]
        if midval < m:
            low = mid + 1
        elif midval > m:
            high = mid - 1
        else:
            # print(mid)
            return mid
    return -1



if __name__ == "__main__":
    aa = [x for x in range(1, 110)]   #生成列表,整数有序
    print(aa)
    b = binarysearch(aa, 18)
    print(b)
    random.shuffle(aa)                #洗牌
    print(aa)
    # print(b)
    # print(random.randint(1, 5))      #随机1~5一个整数
    # print(random.random())           #随机0~1一个浮点数

