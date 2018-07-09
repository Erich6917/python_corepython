# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 
# @Author  : ErichLee ErichLee@qq.com
# @File    : loop.py
# @Comment : 
#            

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def demo1():
    a_list = [1, 2, 3, 4, 5]
    a = [x * 2 for x in a_list if x % 2 == 0]
    print a


demo1()
