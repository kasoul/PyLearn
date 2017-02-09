#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

if __name__ == '__main__':
    s = raw_input('input a string:\n')
    letter_amount = 0
    blank_amount = 0
    digit_amount = 0
    others_amount = 0
    for char in s :
        if char.isalpha():
            letter_amount += 1
        elif char.isspace():
            blank_amount += 1
        elif char.isdigit():
            digit_amount += 1
        else:
            others_amount += 1
    print 'char = %d,space = %d,digit = %d,others = %d' % (letter_amount, blank_amount, digit_amount, others_amount)

