# -*- coding: utf-8 -*-
# @Time    : 2018/4/16 
# @Author  : ErichLee ErichLee@qq.com
# @File    : DateBase.py
# @Commment: 日期类型处理
#

from datetime import timedelta, datetime
from loggerUtil import *


def date_create():
    """
        时间的创建和简答运算
    """
    infos("时间段的创建")
    a = timedelta(days=2, hours=6)
    b = timedelta(hours=4.5)
    c = a + b
    print c.days
    printLine()

    d1 = datetime(2018, 4, 16)
    d2 = datetime(2018, 5, 12)
    ljinfos("时间处理十天之后>", d1 + timedelta(days=10))
    ljinfos("时间之差>", (d2 - d1))
    printLine()


def date_converting():
    text = '2012-09-20'
    y = datetime.strptime(text, '%Y-%m-%d')
    z = datetime.now()


date_converting()
