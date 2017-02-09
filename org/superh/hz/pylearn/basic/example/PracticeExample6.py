#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 题目：斐波那契数列。

# 使用递归
def fib_recursion(n):
	if n==1 or n==2:
		return 1
	return fib_recursion(n-1)+fib_recursion(n-2)

# 输出了第10个斐波那契数列
print fib_recursion(10)

# 使用循环
def fib_loop(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

# 输出前 10 个斐波那契数列
print fib_loop(10)

