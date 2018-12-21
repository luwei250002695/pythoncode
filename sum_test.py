#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Filename : sum_test.py
# author by : edgar

# 用户输入数字
num1 = int(input('输入第一个数字：'))
sum = 0
for i in range(1, num1 + 1):
    if i % 2 == 0:        # i % 2 != 0
        sum += i
print(sum)

sum = 0
# 注意num1 + 1，将0改为1就是奇数求和
for i in range(0, num1 + 1, 2):
    sum += i
print(sum)

sum = 0
i = 0
# 注意num1，将i改为1就是奇数求和
while i <= num1:
    sum += i
    i += 2
print(sum)

# 质数求和
list1 = []
for i in range(1, num1 + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        list1.append(i)
print(list1)




