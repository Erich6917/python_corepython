# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 
# @Author  : ErichLee ErichLee@qq.com
# @File    : merge_clean.py
# @Comment : 多文件重新合并，按照一定的行数或大小重新生成文件
#            

from dateCheckUtil import *
from file_check_util import *
from logger_util import *

reload(sys)
sys.setdefaultencoding('UTF-8')

gbl_counter = 0
gbl_time = str(time.strftime("%Y%m%d%H%M", time.localtime()))  # 当前时间戳
gbl_path_source = ''  # 输入来源
gbl_path_output = ''  # 输出目录
gbl_line_max = 20000  # 合并后每个文件最大行数
gbl_file_merge = None


def init_path():
    """
        初始化输入输出目录
    """
    global gbl_path_source, gbl_path_output
    gbl_path_source = u'source/merge'  # 数据来源
    if not os.path.exists(gbl_path_source):
        infos('未找到目标路径，退出程序！')

    gbl_path_output = u'output/merge'  # 数据输出目录
    if not os.path.exists(gbl_path_output):
        infos('创建输出目录', gbl_path_output)
        os.mkdir(gbl_path_output)


def start():
    # step1 初始化输入输出目录
    init_path()
    global gbl_path_source, gbl_path_output

    # step2 遍历读取文件
    file_list = get_all_files_path_name(gbl_path_source)
    index_read = 0  # 读取文件的行数下标
    index_write = 0  # 生成文件的写入下标
    for file_msg in file_list:
        file_name, file_path = file_msg[0], file_msg[1]
        with open(file_path, 'r') as each_file:
            infos('读取文件[{0}]'.format(file_path))
            f_lines = each_file.readlines()
            index_read, index_write = write_and_clean(f_lines, index_read, index_write)
            infos('关闭文件[{0}]'.format(file_path))
            print_line()


def print_line():
    print '================================'


def write_and_clean(f_lines, index_read, index_write):
    global gbl_line_max
    line_total = len(f_lines)
    infos('读取文件长度[{0}], 写入文件最大长度[{1}],当前文件已写入长度[{2}]'.
          format(line_total, gbl_line_max, index_write))
    # 当写入的文件内容 大于可写入的文件的内容时
    while line_total > gbl_line_max - index_write:
        line_size = gbl_line_max - index_write
        # 即 剩余条数 大于 可容纳条数,则写满后继续循环
        msg_line = f_lines[index_read:index_read + line_size]

        # infos('write continue, size[{0}],msg[{1}]'.format(line_size, msg_line))
        infos('write continue, size[{0}]'.format(line_size))
        write_close_msglist(msg_line)

        line_total = line_total - line_size  # 当前写入文件剩余条数

        index_read = index_read + line_size  # 当前文件 读取下标

        index_write = (index_write + line_size) % gbl_line_max  # 当前文件写入下标

    # 写入剩余内容
    size_last = line_total
    msg_last = f_lines[index_read:]
    infos('write rest msg, size[{0}]'.format(size_last))
    write_msglist(msg_last)

    index_write = (size_last + index_write) % gbl_line_max
    # 读取下标重置为0
    index_read = 0

    return index_read, index_write


def write_msglist(msg_list):
    if msg_list:
        global gbl_file_merge, gbl_path_output, gbl_time, gbl_counter
        gbl_counter += 1

        if not gbl_file_merge:
            str_index = str(gbl_counter)
            file_out_name = 'sina_finance_{0}{1:0>4}.txt'.format(gbl_time, str_index)
            file_out_name = os.path.join(gbl_path_output, file_out_name)
            gbl_file_merge = open(file_out_name, 'a')
            infos('curr file is full , open the new file  ...')
        gbl_file_merge.writelines(msg_list)


def write_close_msglist(msg_list):
    write_msglist(msg_list)

    global gbl_file_merge
    if gbl_file_merge:
        gbl_file_merge.close()
        gbl_file_merge = None


if __name__ == '__main__':
    start_time = currDateFormate()
    print 'START {0}'.format(start_time)
    print_line()

    start()

    print_line()
    end_time = currDateFormate()
    print 'END {0},COST > {1}'.format(end_time, (end_time - start_time)),
