# -*- coding: utf-8 -*-
# @Time    : 2018/1/5
# @Author  : LIYUAN134
# @File    : IOBASE.py
# @Commment:
#
import os
import sys
from util.loggerUtil import *

reload(sys)
sys.setdefaultencoding('utf-8')


def io_open():
    """
        文件打开方式，
        使用with open 结构，文件读取完自动关闭。
        使用open生命文件，需手动关闭文件
    """
    file_path = "source/voice1.txt"
    with open(file_path, 'rt') as f:
        data = f.read()
        print "[", data, "]"
    amsg = "读写文本文件一般来讲是比较简单的。但是也几点是需要注意的。首先，在例子程\
    序中的with 语句给被使用到的文件创建了一个上下文环境，但with 控制块结束时，\
    文件会自动关闭.你也可以不使用with 语句，但是这时候你就必须记得手动关闭文件"
    infos(amsg)

    f = open(file_path, 'rt')
    data = f.read()
    f.close()

    amsg = "文件打开方式大概可以分成三种 [r w a] 另外一种b指的是二进制文件 " \
           "r>读 w>写 a>追加到文章最后 具体组合如下：\n" \
           "R  只读 \n" \
           "W  只写 覆盖原有文件 \n" \
           "A  只写 追加结尾写入 \n" \
           "W+ 读写 覆盖原有文件 \n" \
           "R+ 读写 追加开头写入 \n" \
           "A+ 读写 追加结尾写入 \n"

    infos(amsg)


io_open()


def file_existence():
    path_curr = u'source'
    if not os.path.exists(path_curr):
        os.makedirs(path_curr)

    counter = len(os.listdir(path_curr))
    print counter
    print "IS DIR", os.path.isdir(path_curr)
    print "IS FILE", os.path.isfile(path_curr)


def write_demo1():
    with open('somefile.txt', 'w+') as f:
        f.write('write \n')
        f.write('write again \n')


def read_demo2():
    files = open('lm_voice_001.txt', 'r')
    print len(files.readlines())
    total = 0
    for line in open('voice1.txt', 'r'):
        # print line
        total += 1
    print total

# if __name__ == '__main__':
#     read_demo2()
