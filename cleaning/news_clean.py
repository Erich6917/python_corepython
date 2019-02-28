# -*- coding: utf-8 -*-
# @Time    : 2018/6/13 
# @Author  : ErichLee ErichLee@qq.com
# @File    : news_clean.py
# @Comment : 新闻数据初步清洗
#            过滤行数过少或者页面js部分代码
#            

import re

from util.file_check_util import *
from logger_util import *

reload(sys)
sys.setdefaultencoding('utf-8')

gbl_path_source = ''
gbl_path_output = ''


def stop():
    exit()


def init_path():
    global gbl_path_source, gbl_path_output
    gbl_path_source = u'source/news'  # 数据来源
    if not os.path.exists(gbl_path_source):
        infos('未找到目标路径，退出程序！')
        stop()

    gbl_path_output = u"output/news"  # 数据输出目录
    if not os.path.exists(gbl_path_output):
        os.mkdir(gbl_path_output)


def bool_write(line):
    regex = r'[ ,\.#%''\+\*\-:;^_`=a-zA-Z{}()\[\]\"]+'
    if line is None:
        return False
    line = line.strip()  # 删除\s
    if line == '':
        return False
    if len(line) < 30:  # 中文占3个长度
        return False
    if re.match(r" +", line):
        return False
    if re.match(r"\s+", line):
        return False
    if re.match(regex, line):
        return False
    return True


def clean_and_write(lines, path_clean):
    try:
        file_clean = open(path_clean, 'a')

        counter = 0
        for line in lines:
            counter += 1
            # if counter > 10000:
            #     return
            if bool_write(line):
                # print counter, '>', line
                file_clean.write(line)
            else:
                pass

    finally:
        if file_clean:
            file_clean.close()


def start_parse():
    global gbl_path_source, gbl_path_output
    files = get_all_files_path_name(gbl_path_source)
    for file_msg in files:
        file_name, path_file = file_msg[0], file_msg[1]
        # path_file = os.path.join(gbl_path_source, file_name)
        path_clean = os.path.join(gbl_path_output, file_name)
        with open(path_file, 'r') as each_file:
            lines = each_file.readlines()
            print file_name, len(lines)
            clean_and_write(lines, path_clean)


def start():
    init_path()

    start_parse()


if __name__ == '__main__':
    start()
