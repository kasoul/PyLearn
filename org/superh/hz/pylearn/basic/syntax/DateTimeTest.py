#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 日期时间测试
import time,calendar;  # 引入time模块

ticks = time.time()     # 得到的ticks是一个float
print "当前时间戳为:", ticks

localtime = time.localtime(time.time())     # 得到的localtime是一个tuple
print "本地时间为 :", localtime

localtime = time.asctime(localtime)     # 将tuple转化为string
print "本地时间为 :", localtime

# 格式化成2016-03-20 11:45:39形式
s = time.strftime("%Y-%m-%d %H:%M:%S",  time.localtime())
print s

# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
b = "2016-03-25 12:55:46"
print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))
print time.mktime(time.strptime(b, "%Y-%m-%d %H:%M:%S"))

cal = calendar.month(2017, 1)
print "以下输出2016年1月份的日历:"
print cal;
