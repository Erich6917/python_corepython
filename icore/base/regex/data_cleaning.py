# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 
# @Author  : ErichLee ErichLee@qq.com
# @File    : data_cleaning.py
# @Comment : 
#            

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')


def start():
    lines = open(u'data.txt', 'r')
    for line in lines:
        list = re.findall('href="(thunder://[^"]+)"', line)
        for msg in list:
            print msg


start()
