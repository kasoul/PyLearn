#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 题目：暂停一秒输出

import time

dic ={"aaa" : 44,"bbb":55}
for key,value in dict.items(dic):
    print key, value
    time.sleep(1)  # 暂停 1 秒