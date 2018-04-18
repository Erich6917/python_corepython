# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 
# @Author  : ErichLee ErichLee@qq.com
# @File    : loggerUtil.py
# @Commment: 
#            
import logging


def infos(*args):
    """
    :comment 同时print 和 打印日志
    :type args: object
    """
    if args:
        for each in args:
            print each,
        print
        logging.info(args)


def ljinfos(lmgs, *args):
    """
    :param lmgs: 打印头 需要格式化长度
    :param args: 变量参数依次打印
    """
    if lmgs:
        print '[ ' + lmgs.ljust(30) + ' ]:',
    else:
        print '[ ' + "".ljust(30) + ' ]:',

    if any(args):
        for each in args:
            print each,
    print


def printLine():
    print '================================'
