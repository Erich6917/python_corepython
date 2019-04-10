# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 
# @Author  : ErichLee ErichLee@qq.com
# @File    : file_rename.py
# @Comment : 文件重命名
#            

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import os


def file_rename():
    movie_name = os.listdir('C:/Data/movie/movie_start/dajiangdahai')
    for temp in movie_name:
        new_name = temp.replace(u'D江大河-14.mp4', u'dajiangdahai')
        print temp.decode('utf-8'),type(temp)
        os.rename(movie_name+'/'+temp, movie_name+'/'+new_name)


file_rename()
