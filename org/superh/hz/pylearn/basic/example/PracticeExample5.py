#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。

x = int(raw_input('x:\n'))
y = int(raw_input('y:\n'))
z = int(raw_input('z:\n'))

list = [x, y, z]
# 选择排序
"""
for i in range(len(list)):
    for j in range(i+1, len(list)):
        if(list[i] > list[j]):
            min = list[i];
            list[i] = list[j];
            list[j] = min;
"""
list.sort()
print list

