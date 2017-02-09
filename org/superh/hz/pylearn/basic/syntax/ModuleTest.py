#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 模块测试

import sys
import Module1
import module
# from Module2 import * 为什么不能部分导入？

if __name__ == '__main__':
    print sys.path
    Module1.printtest1("Jackie")
    module1Content = dir(Module1)
    print module1Content;

    module.printtest11()
    module.printtest12()
    module.printtest13()


