# -*- coding: utf-8 -*-
# @Time    : 2018/1/5
# @Author  : LIYUAN134
# @File    : io_test.py
# @Commment:
#

import os


def write_demo1():
    with open('somefile.txt', 'w+') as f:
        f.write('write \n')
        f.write('write again \n')


def read_demo1():
    with open('somefile.txt', 'rt') as f:
        data = f.read()
        print data


def read_demo2():
    files = open('lm_voice_001.txt', 'r')
    print len(files.readlines())
    total = 0
    for line in open('demo2.txt', 'r'):
        # print line
        total += 1
    print total


if __name__ == '__main__':
    read_demo2()


def file_create():
    path_curr = u'src/中医'
    if not os.path.exists(path_curr):
        os.makedirs(path_curr)

    counter = len(os.listdir(path_curr))
    print counter
