# -*- coding: utf-8 -*-
# @Time    : 2017/11/23
# @Author  : LIYUAN134
# @File    : exception.py
# @Commment:
#


def exp1():
    try:
        f = open('', 'r')
    except IOError, e:
        print e
    finally:
        print 'close'

    print 'exp1...'
    if 1 == 1:
        raise Exception('raise error', '')

    print 'end'


exp1()
