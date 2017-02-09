#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 基本数据类型-字符串，变量定义

str = "hello world."

print str            # 输出完整字符串
print str[0]         # 输出字符串中的第一个字符
print str[2:5]       # 输出字符串中第三个至第五个之间的字符串,包含头下标2，不包含尾下标5
print str[2:]        # 输出从第三个字符开始的字符串
print str * 2        # 输出字符串两次
print str + "TEST"  # 输出连接的字符串

print str[-5]
print str[-5:-1]     # -5，-1是从右到左索引的下表
print str[-1:-5]     # 打印还是要从左到右打印，这条打印不出来
