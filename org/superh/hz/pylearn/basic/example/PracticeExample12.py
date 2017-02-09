#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 题目：判断101-200之间有多少个素数，并输出所有素数。

def isPrime(n):
    for i in range(2,n):
        if (n % i == 0):
            return False
    return True

count = 0;
for i in range(101,201):
    if(isPrime(i)):
        print i
        count += 1
print "prime amount is %d." % count
