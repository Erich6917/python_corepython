# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 
# @Author  : ErichLee ErichLee@qq.com
# @File    : file_rename.py
# @Comment : 文件重命名
#
import re
import sys
from xpinyin import Pinyin
import util.file_check_util as file_util

reload(sys)
sys.setdefaultencoding('utf-8')

import os


def file_rename(path_old, path_new):
    os.rename(path_old, path_new)


# 把当前目录下的文件 重命名
def start_file_rename():
    path = u'D:/yuan/movie/Att'
    movie_name = os.listdir(path)
    for temp in movie_name:
        new_name = temp.replace(u'D到烟暖雨收第三季', u'DDyys')
        file_rename(path + '/' + temp, path + '/' + new_name)


#
def start_file_read_create_rename():
    source_path = u'source'
    output_source = u'output'
    file_list = file_util.get_curr_files(source_path)
    p = Pinyin()
    for file_name, file_path in file_list:
        # print file_name, file_path
        name_old, name_seq = file_name.split('-')[0], file_name.split('-')[1]
        name_deal = re.sub('[a-zA-Z]', '', name_old)
        if name_deal:
            folder_name = p.get_pinyin(name_deal)
            file_name = '{}-{}'.format(folder_name, name_seq)
        else:
            folder_name = name_old

        # 创建目标路径
        output_path = os.path.join(source_path, output_source, folder_name)
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        print 'rename', file_path, os.path.join(output_path, file_name)
        file_rename(file_path, os.path.join(output_path, file_name))
        # rename
        # p = Pinyin()
        # print p.get_pinyin(u"上海r")


def check_contain_chinese(check_str):
    for ch in check_str.decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


def is_Chinese(word):
    if u'\u4e00' <= word <= u'\u9fff':
        return True
    return False


def get_pinyin(word_chinese):
    p = Pinyin()
    rt_msg = []
    for word in word_chinese:
        ex_word = word
        if is_Chinese(ex_word):
            ex_word = p.get_pinyin(ex_word)
        rt_msg.append(ex_word)
    return ''.join(rt_msg)


# 替换所有中文
def start_file_create_all():
    source_path = u'C:/FFOutput/wav'
    output_source = u'C:/FFOutput/wav/aout'

    file_list = file_util.get_curr_files(source_path)
    for file_name, file_path in file_list:

        matcher = re.match('(.*)(\\.[^.]+)', file_name)
        if matcher:
            name, ends = matcher.group(1), matcher.group(2)

            new_name = '{}{}'.format(get_pinyin(name), ends)
            # 创建目标路径
            output_path = os.path.join(source_path,output_source)
            if not os.path.exists(output_path):
                os.makedirs(output_path)

            print 'rename', file_path, os.path.join(output_path, new_name)
            file_rename(file_path, os.path.join(output_path, new_name))
            # rename
            # p = Pinyin()
            # print p.get_pinyin(u"上海r")
        else:
            print 'ERROR 匹配失败'


# start_file_read_create_rename()
start_file_create_all()
