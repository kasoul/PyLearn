#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 类继承测试
import ClassA

class SubEmployee(ClassA.Employee):

    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age
        ClassA.Employee.empCount += 1

    def __del__(self):
        class_name = self.__class__.__name__


subemp1 = SubEmployee("Zara", 2000, 25)
subemp1.displayEmployee()