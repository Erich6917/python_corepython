# -*- coding: utf-8 -*-
# @Time    : 2018/6/14
# @Author  : LIYUAN134
# @File    : resolve_clean.py
# @Comment : 大文件拆分小文件
#            
import re

from file_check_util import *

reload(sys)
sys.setdefaultencoding('utf-8')

line_total = 0
writing_file = None


def one_to_many():
    global line_total, writing_file
    line_max = 50000  # 合并后每个文件最大行数
    line_seq = 1  # 合并后的多文件序列号，初始化为1
    pre_writing_name = ''  # 遍历文件记录前一个文件名称

    path_source = u'source/resolve'  # 数据来源
    path_output = u"output/resolve"  # 数据输出目录
    if not os.path.exists(path_output):
        os.mkdir(path_output)

    file_list = get_all_files(path_source)  # 获取数据来源目录下所有文件

    for filename in file_list:

        file_path = path_source + "/" + filename

        each_file = open(file_path, 'r')
        flines = each_file.readlines()
        writing_name = re.sub('_.*|\\..*', '', filename)  # 获取多文件前缀

        if pre_writing_name != writing_name:
            line_seq = 1  # 当前一个文件名称和本次文件名称不同时，文件序号重置
            pre_writing_name = writing_name  # 文件名称赋值给前一个文件用于下次循环
            line_total = 0

        curr_line = line_total + len(flines)
        print line_total, curr_line

        writing_filename = path_output + '/' + writing_name + u'_' + str(line_seq) + '.txt'
        writing_file = open(writing_filename, 'a')
        print '编辑文件', writing_filename

        if curr_line <= line_max:
            for line in flines:
                try:
                    writing_file.write((line.split('@'))[2])
                except Exception, e:
                    print "原文本格式错误，跳过继续", e
            line_total = curr_line
        else:

            for line in flines:
                try:
                    line_total += 1
                    writing_file.write((line.split('@'))[2])
                except Exception, e:
                    print "原文本格式错误，跳过继续", e

                if line_total >= line_max:
                    line_seq += 1
                    writing_file.flush()
                    writing_file.close()  # 关闭老文件

                    writing_filename = path_output + '/' + writing_name + u'_' + str(line_seq) + '.txt'
                    writing_file = open(writing_filename, 'a')
                    print '创建新文件:', writing_filename

                    line_total = 0  # 重置

    print '====================================='


if __name__ == '__main__':
    one_to_many()
