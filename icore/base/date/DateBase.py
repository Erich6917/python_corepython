# -*- coding: utf-8 -*-
# @Time    : 2018/4/16 
# @Author  : ErichLee ErichLee@qq.com
# @File    : DateBase.py
# @Commment: 日期类型处理
#

from datetime import timedelta, datetime, date
from util.logger_util import *
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

    ljinfos("4. 获取当天开始和结束时间")
    # infos(datetime.combine(date.today(), time.min()))

    ljinfos("5. 获取两个datetime的时间差")
    infos((datetime(2015, 1, 13, 12, 0, 0) - datetime.now()).total_seconds())

    ljinfos("6. 获取本周/本月/上月最后一天")
    today = date.today()
    sunday = today + timedelta(6 - today.weekday())
    ljinfos("本周末》", sunday)

    first = date(day=1, month=today.month, year=today.year)
    lastMonth = first - timedelta(days=1)
    ljinfos("上月末》", lastMonth)


def date_change():
    """
    几个关系之间的转化

    Datetime Object / String / timestamp / time tuple
    """
    ljinfos("datetime -> string")
    infos(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    ljinfos("string -> datetime")
    infos(datetime.strptime("2014-12-31 18:20:10", "%Y-%m-%d %H:%M:%S"))

    ljinfos("datetime -> timetuple")
    infos(datetime.now().timetuple())

    ljinfos("timetuple -> datetime")

    ljinfos("datetime -> date")
    infos(datetime.now().date())

    ljinfos("date -> datetime")
    infos(date.today())
    # today = date.today()
    # datetime.combine(today, time())

    ljinfos("datetime -> timestamp")
    now = datetime.now()
    timestamp = time.mktime(now.timetuple())
    infos(timestamp)

    ljinfos("timestamp -> datetime")
    infos(datetime.fromtimestamp(1421077403.0))

date_change()


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
