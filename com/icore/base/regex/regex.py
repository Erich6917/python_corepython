# -*- coding: utf-8 -*-
# @Time    : 2017/11/27 
# @Author  : LIYUAN134
# @File    : regex.py
# @Commment: 正则表达式demo
#            

import re


def printLine():
    print '================================='


def my_match(regex, msg):
    rt = re.match(regex, msg)
    if rt:
        print 'SUCCESSED !  => ', rt.group()
    else:
        print 'NOT MATCH !'
    print '     msg:', msg, '  /regex:', regex
    printLine()


def my_search(regex, msg):
    rt = re.search(regex, msg)
    if rt:
        print 'SUCCESSED !  => ', rt.group()
    else:
        print 'NOT MATCH !'
    print '     msg:', msg, '  /regex:', regex
    printLine()


# re.match函数
# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。

def match_demo1():
    msg = 'liyuan134.pingan.com.cn'
    regex = 'liyuan'
    my_match(regex, msg)

    regex = 'com'
    my_match(regex, msg)

    regex = '[a-z0-9]+\.pingan\.com$'
    # 结尾添加$，表示全匹配，开头^可以省略
    my_match(regex, msg)


# match_demo1()


# match_demo1 结果分析：
# match匹配的条件为：1.开头匹配 2.全匹配
# 但开头匹配容易引起误导，我们往往需要全匹配来判断文本是否满足条件
# java正则中match为全匹配
# python中为了弥补这点，需要在结尾添加$符号，标识结尾，即表示全匹配


# re.search方法
# re.search 扫描整个字符串并返回第一个成功的匹配。
def search_demo1():
    msg = 'liyuan134.pingan.com.cn'

    regex = 'liyyyyyyy'
    my_search(regex, msg)

    regex = '[0-9]'
    my_search(regex, msg)  # 返回第一个数字

    regex = '[a-zA-Z]+'
    my_search(regex, msg)  # 返回一个字符串


# search_demo1()


def findall_demo1():
    msg = 'Liyuan134李源Liyuan001利源Liyuan123李渊'
    regex = '[a-zA-Z0-9]+'
    rt = re.findall(regex, msg)
    if rt:
        for single in rt:
            print 'UM:', single
            # 循环输出所有符合条件的内容
    else:
        print 'not find'


# findall_demo1()


def split_demo1():
    msg = 'liyuan134.pingan.com.cn'
    regex = '\.'
    rt = re.split(regex, msg)
    # 点号分割字符串
    for each in rt:
        print each


# split_demo1()


# 高级应用1：替换文本
def addBlank(matched):
    value = matched.group('value')
    return str(value) + ' '


def sub_demo():
    msg = 'Liyuan134.pingan.com.cn #Email 我的公司邮箱'.decode('utf8')

    regex = '#.*$'
    # 类似于 JAVA中的 replaceAll
    rt = re.sub(regex, '', msg)
    print 'SUCCESS: => ', rt
    printLine()

    # msg = '1234fff56789,aabbcc12345ddd6789,w'
    msg = open('number.txt', 'r').read().decode('utf8')
    rt = re.sub('(?P<value>\d|[,.])', addBlank, msg)
    print rt


sub_demo()


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


findProvinces()
