# -*- coding: utf-8 -*-
# @Time    : 2018/6/26
# @Author  : ErichLee ErichLee@qq.com
# @File    : merge.py
# @Comment :
#

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import os

from util.file_check_util import *

if __name__ == '__main__':
    source = 'source'
    file_list = get_all_files_path_name(source)
    for file in file_list:
        print 'NAME>{},PATH>{}'.format(file[0], file[1])
