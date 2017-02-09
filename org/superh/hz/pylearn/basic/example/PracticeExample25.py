#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 题目：求1+2!+3!+...+20!的和。

sn = []
multiplicative = 1
for i in range(1,21):
    multiplicative = multiplicative * i
    sn.append(multiplicative)

print sn
print reduce(lambda x,y:x+y, sn)


