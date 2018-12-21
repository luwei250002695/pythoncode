#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Filename : huiwenshu_test.py
# author by : edgar

#字符型
str = 'aabbcbbaa'
i = len(str) - 1
j = 0
while j < i:
    if str[j] == str[i]:
        i -= 1
        j += 1
        pass
    else:
        print('False')
        break
else:
    print('Ture')


def string_reserved1(parameter_str):
    m = parameter_str[::-1]
    return m == parameter_str

def string_reserved2(parameter_str):
    list_str = list(parameter_str)
    print(list_str)
    list_str.reverse()
    return list_str

# print(string_reserved1(str))
# print(string_reserved2(str))

