#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
# 低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万
# 元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

i = int(raw_input('净利润:'))
profitList = [100, 60, 40, 20, 10, 0]
rateList = [0.01, 0.015, 0.03, 0.05, 0.075, 0.10]
bonus = 0

for index in range(0, 6):
    if(i > profitList[index]):
        bonus += (i-profitList[index]) * rateList[index]
        print "index:", index
        print "bonus in this level:", (i-profitList[index]) * rateList[index]
        i = profitList[index]

print "total bonus is: %d" % bonus
