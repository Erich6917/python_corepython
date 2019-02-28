# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 
# @Author  : ErichLee ErichLee@qq.com
# @File    : file_counter.py
# @Comment : 
#            

import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')


def get_all_files(path_source='.'):
    file_list = []
    for root, dirs, files in os.walk(path_source):
        for filename in files:
            if filename.endswith('.wav'):
                file_list.append(filename)
    return file_list


def file_wav_counter():
    path = 'C:\Users\Administrator\Desktop\shenfenzheng'
    wav_list = get_all_files(path)
    print len(wav_list)


def msg_add_block():
    rt_file = open('script-rt.txt', 'a+')
    with open('script.txt', 'a+') as file:
        lines = file.readlines()
        for line in lines:
            p1, p2 = line[0:19], line[19:]
            msg = p1 + "   " + p2
            rt_file.write(msg)


msg_add_block()
