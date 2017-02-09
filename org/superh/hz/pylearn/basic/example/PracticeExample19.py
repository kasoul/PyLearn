#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

from sys import stdout

count = 0
for i in range(2,1001):
    s = i
    t = 0
    jn = []
    for j in range(1,i):
        if(i%j == 0):
            t += j
            s -= j
            jn.append(j)
    if(s == 0):
        print i
        print jn
        count += 1

print "amount is %d" % count

