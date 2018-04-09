# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 
# @Author  : LIYUAN134
# @File    : common.py
# @Commment: 
#            

import time


def start():
    index = 10
    while index > 0:
        print '你好', index
        index -= 1
        time.sleep(1)


if __name__ == '__main__':
    start()
