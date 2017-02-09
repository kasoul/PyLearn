#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

numberList = [1, 2, 3, 4]
resultList = []

for i in numberList:
    for j in numberList:
        for k in numberList:
            if(i != j and j != k and i != k):
                resultList.append(str(i)+str(j)+str(k))

print "number count: %d" % len(resultList)
for num in resultList:
    print num
