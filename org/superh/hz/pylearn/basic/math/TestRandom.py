#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 测试随机函数

from random import randint
from random import sample
from random import randrange
from random import random
from random import uniform

print randint(10, 20)
print range(10,20,2)
print range(20,10,-1)
print sample(range(10,20,1), 5)
print randrange(10,20)
print random()
print uniform(10,20)

chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
print ''.join(sample(chars, 20))
