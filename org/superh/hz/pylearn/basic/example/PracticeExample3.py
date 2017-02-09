#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 题目：一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
import math

for number in range(0, 10000):
    x = int(math.sqrt(number + 100))
    y = int(math.sqrt(number + 268))
    if (x * x == number + 100) and (y * y == number + 268):
        print number
