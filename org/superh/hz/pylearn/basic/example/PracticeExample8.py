#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 题目：输出9*9乘法口诀表。

for i in range(1, 10):
    for j in range(1, 10):
        print "%d * %d = %d" % (i,j,i*j)

