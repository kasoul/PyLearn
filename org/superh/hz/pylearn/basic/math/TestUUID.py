#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 测试UUID产生

import uuid
import hashlib
import time

def create_uuid():   #通过UUID的方式创建
    return str(uuid.uuid1())

def create_md5():    #通过MD5的方式创建
    m = hashlib.md5()
    m.update(str(time.time()))
    return m.hexdigest()

if __name__ == '__main__':
    print(create_uuid())
    print(create_md5())