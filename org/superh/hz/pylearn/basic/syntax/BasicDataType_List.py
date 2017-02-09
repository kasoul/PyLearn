#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 基本数据类型-列表，变量定义

from random import *

list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print list              # 输出完整列表
print list[0]           # 输出列表的第一个元素
print list[1:3]         # 输出第二个至第三个的元素
print list[2:]          # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2      # 输出列表两次
print list + tinylist   # 打印组合的列表

doubleTinyList = tinylist * 2
print doubleTinyList

print "-------------------------------------I am split line--------------------------------------"

numlist = range(0,10,2)
print numlist

print randrange(0,20)
print randint(0,20)

data = [randint(-10, 10) for x in range(10)]   # 利用列表生成式生成列表
print data
filterData1 = filter(lambda x: x >= 0, data)    # 利用lambda表达式构建传递函数
print filterData1
filterData2 = [x for x in data if x >= 0]       # 利用列表生成式过滤
print filterData2