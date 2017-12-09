# -*- coding: utf-8 -*-
# @Time    : 2017/11/27 
# @Author  : LIYUAN134
# @File    : regex2.py
# @Commment: 
#            

import re


def printLine():
    print '================================='


# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
def t_match():
    msg = 'liyuan134.com.cn'
    regex = 'liyuan'

    rt1 = re.match(regex, msg)
    rt2 = re.match(regex, msg).span()
    if rt1:
        print 're.match(regex, msg) => '
        print ' rt1 => ', rt1
        print ' rt1.group() => ', rt1.group()
    else:
        'rt1 not match'
    printLine()
    if rt2:
        print 're.match(regex, msg).span() =>'
        print ' rt2 => ', rt2
        # print ' rt2.group() => ', rt2.group() #error
    else:
        print 'rt2 not match'


t_match()


def findAllProvinces():
    msg = open('BaiduMap_cityCenter.txt', 'r').read().decode('utf8')
    print msg
    # way 1 =================
    # out = re.findall(u'[\u4e00-\u9fa5]+', msg, re.M | re.I)
    # if out:
    #     print '========'
    #     for ii in out:
    #         print ii
    # way 1 =================
    # \"([0-9.,|]+)\"
    out = re.findall(u'([\u4e00-\u9fa5]+)\",\s*g:\"([0-9.,|]+)\"', msg, re.M | re.I)
    for ii in out:
        print ii[0], ii[1]

        # if out:
        #     print 'result:'
        #     print out.group()
        # else:
        #     print 'not found'
        # n:"淮南", g:"117.018639,32.642812|13"


def findProvinces():
    msg = open('BaiduMap_cityCenter.txt', 'r').read().decode('utf8')
    out = re.findall(u'\"([\u4e00-\u9fa5]+)\",\s*g:\"([0-9.,|]+)\"', msg, re.M | re.I)
    for ii in out:
        print ii[0], ii[1]

# findProvinces()
