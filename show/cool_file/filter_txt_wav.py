# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 
# @Author  : ErichLee ErichLee@qq.com
# @File    : filter_txt_wav.py
# @Comment : 删除没有找到对应txt的wav
#            

import sys
import os
import re
import util.file_check_util as file_util

reload(sys)
sys.setdefaultencoding('utf-8')


def start():
    path_list = [
        u'D:\movie-output\Acut&text\HW之破晓之战-03-180-3611-pic-dir-full',
    ]

    path_list = get_all_dirs(u'D:\movie-output\Acut&text')
    for path in path_list:
        start_delete(path)


def get_all_dirs(path_source='.'):
    # rt_list = []
    # for filename in os.listdir(path_source):
    #     rt_list.append(os.path.join(path_source, filename))
    # return rt_list
    return [os.path.join(path_source, filename) for filename in os.listdir(path_source)]


def get_all_files_path_name(path_source='.'):
    file_list = []
    for root, dirs, files in os.walk(path_source):
        for filename in files:
            if filename.endswith('.txt'):
                file_msg = filename, os.path.join(root, filename), root
                file_list.append(file_msg)
    return file_list


def start_delete(path):
    file_list = file_util.get_all_files_path_name(path)
    if not file_list:
        raise Exception('Not Found!')

    rm_list = []

    for file in file_list:
        file_name, file_path = file[0], file[1]
        with open(file_path) as file_txt:
            msg = file_txt.readline()
            if msg is None or msg == '':
                file_name = re.sub('\\..*', '', file_name)
                rm_path_jpg = u'{}/{}.jpg'.format(path, file_name)
                rm_list.append((file_path, rm_path_jpg))
    print 'delete.... ', len(rm_list), path
    for each in rm_list:
        p1, p2 = each[0], each[1]
        os.remove(p1)
        os.remove(p2)


start()
