# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 
# @Author  : ErichLee ErichLee@qq.com
# @File    : file_common_util.py
# @Comment : 
#            

import sys
import util.file_check_util as file_util
import os

reload(sys)
sys.setdefaultencoding('utf-8')


def move_move():
    path = u'C:/Personal/workspace/mygit_py2/littlespider/start/ximalaya/source/audio/青年圆桌派'
    file_list = file_util.get_all_files_path_name(path)
    for file_name, file_path, file_root in file_list:
        # print(file_name, file_path, file_root)
        file_util.move_file(file_path, os.path.join(path, file_name))


def move_to_curr(path):
    file_list = file_util.get_all_files_path_name(path)
    for file_name, file_path, file_root in file_list:
        # print(file_name, file_path, file_root)
        file_util.move_file(file_path, os.path.join(path, file_name))
