# -*- coding: utf-8 -*-
# @Time    : 2018/6/1 
# @Author  : ErichLee ErichLee@qq.com
# @File    : pyinstallDemo.py
# @Comment : 
#            

import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')


def getCurrentPath():
    if getattr(sys, 'frozen', False):
        apply_path = os.path.dirname(sys.executable)
    elif __file__:
        apply_path = os.path.dirname(__file__)
    return apply_path


def start():
    path = getCurrentPath() + '/source'

    for file in os.listdir(path):
        print file


if __name__ == '__main__':
    start()
