# -*- coding: utf-8 -*-
# @Time    : 2018/1/5
# @Author  : LIYUAN134
# @File    : io_test.py
# @Commment:
#


def write_demo1():
    with open('somefile.txt', 'w+') as f:
        f.write('write \n')
        f.write('write again \n')


def read_demo1():
    with open('somefile.txt', 'rt') as f:
        data = f.read()
        print data


write_demo1()
read_demo1()
