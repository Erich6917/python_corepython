# -*- coding: utf-8 -*-
# @Time    : 2018/1/11 
# @Author  : LIYUAN134
# @File    : timer.py
# @Commment: 
#            
from datetime import datetime, timedelta


def demo_time1():
    a = datetime(2012, 9, 23)
    print a
    print(a + timedelta(days=10))

    b = datetime(2012, 12, 21)
    d = b - a
    print d.days

    now = datetime.today()
    print 'NOW:', now


def demo_change():
    text = '2012-09-20'
    y = datetime.strptime(text, '%Y-%m-%d')
    z = datetime.now()
    diff = z - y
    print diff


demo_change()
