# -*- coding: utf-8 -*-
# @Time    : 2019/6/5 
# @Author  : ErichLee ErichLee@qq.com
# @File    : s0_move.py
# @Comment : 
#            

import sys
import show.cool_file.file_common_util as file_utl

reload(sys)
sys.setdefaultencoding('utf-8')


def file_move():
    path = 'E:/clean-fayuan/Batch4-20190621'
    file_utl.move_to_curr(path)

file_move()