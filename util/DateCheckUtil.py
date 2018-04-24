# -*- coding: utf-8 -*-
# @Time    : 2017/12/21
# @Author  : ErichLee ErichLee@qq.com
# @File    : DateCheckUtil.py
# @Commment: 日期转换常用工具列
#
import datetime
import time


def __curr_time():
    print time.time()
    print time.localtime((time.time()))
    print time.localtime()

    print time.strftime("%Y-%m-%d %H:%M:%S %Y", time.localtime())

    print datetime.datetime.now()


def curr_date_str():
    return time.strftime("%Y-%m-%d", time.localtime())


def curr_date_str2():
    return time.strftime("%Y%m%d", time.localtime())
