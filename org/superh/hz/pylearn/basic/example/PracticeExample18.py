#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。

if __name__ == '__main__':
    Tn = 0
    Sn = []
    a = int(raw_input('input number a=:'))
    n = int(raw_input('input amount n=:'))
    for i in range(n):
        Tn = Tn + a
        a = a*10
        Sn.append(Tn)
    print Sn
    sumSn = reduce(lambda x,y : x+y,Sn)
    print sumSn