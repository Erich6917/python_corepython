# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 
# @Author  : LIYUAN134
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


def printLine():
    print '================================'
