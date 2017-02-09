#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 基本数据类型-字典，变量定义

from random import randint

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print dict['one']  # 输出键为'one' 的值
print dict[2]  # 输出键为 2 的值
print tinydict  # 输出完整的字典
print tinydict.keys()  # 输出所有键
print tinydict.values()  # 输出所有值

print len(tinydict)

students = {x: randint(30, 100) for x in xrange(1, 11)}     # 利用列表生成式生成字典
print students
filterStudents = {k:v for k,v in students.items() if v >= 80}   # 利用列表生成式过滤
print filterStudents
