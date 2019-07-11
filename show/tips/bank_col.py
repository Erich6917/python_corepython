# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 
# @Author  : ErichLee ErichLee@qq.com
# @File    : bank_col.py
# @Comment : 
#            

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def bef_type1():
    bef_mon = 60
    bef_month = 24
    money = 5


def bef_type2():
    money = 50000
    bef_pay = 2325.75
    bef_month = 24
    print bef_pay * bef_month

    total = 0
    for month in range(1, 25):
        last = money - month * bef_pay
        if last < 0:
            return
        bef = last * 60 / 10000.0
        total += bef
        print month, last, bef, total


bef_type2()
