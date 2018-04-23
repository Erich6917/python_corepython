# -*- coding: utf-8 -*-
# @Time    : 2018/4/16 
# @Author  : ErichLee ErichLee@qq.com
# @File    : DateBase.py
# @Commment: 日期类型处理
#

from datetime import timedelta, datetime, date
from util.loggerUtil import *
import time


def date_type():
    """
    时间转换涉及类型
    """
    ljinfos("1/5 datetime")
    now = datetime.now()
    infos(now)
    infos(type(now))

    ljinfos("2/5 timestamp")
    ctime = time.time()
    infos(ctime)
    infos(type(ctime))

    ljinfos("3/5 time tuple")
    ttime = time.localtime()
    infos(ttime)
    infos(type(ttime))

    ljinfos("4/5 string")
    stime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    infos(stime)
    infos(type(stime))

    ljinfos("5/5 datetime")
    ddate = datetime.now().date()
    infos(ddate)
    infos(type(ddate))


def date_base():
    ljinfos("1. 获取当前datetime")
    infos(datetime.now())

    ljinfos("2. 获取当天date")
    infos(date.today())

    ljinfos("3. 获取明天/前N天")
    infos(">>>明天 ")
    infos(date.today() + timedelta(days=1))
    infos(">>>三天前")
    infos(datetime.now() - timedelta(days=3))



date_base()


def date_create():
    """
        时间的创建和简答运算
    """
    infos("时间段的创建")
    a = timedelta(days=2, hours=6)
    b = timedelta(hours=4.5)
    c = a + b
    print c.days
    println()

    d1 = datetime(2018, 4, 16)
    d2 = datetime(2018, 5, 12)
    ljinfos("时间处理十天之后>", d1 + timedelta(days=10))
    ljinfos("时间之差>", (d2 - d1))
    println()


def date_converting():
    """
        时间类型转换，后续新增时间工具类
    """
    text = '2012-09-20'
    y = datetime.strptime(text, '%Y-%m-%d')
    z = datetime.now()
    infos(z - y)
