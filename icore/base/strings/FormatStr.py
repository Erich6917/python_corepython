# -*- coding: utf-8 -*-
# @Time    : 2018/4/27 
# @Author  : ErichLee ErichLee@qq.com
# @File    : FormatStr.py
# @Commment: 字符串格式化输出
#            

import sys
from util.logger_util import *

reload(sys)
sys.setdefaultencoding('utf-8')


def str_old():
    """
    采用“%”作为格式化输出的标记
    """
    print("The first number: %5d, the second number: %8.2f" % (123, 456.789))


def str_format1():
    infos("First argument: {0}, second one: {1}".format(47, 11))
    msg = "{0:^10}\t{1:{3}^10}\t{2:^10}"  # # {1:{3}^10} 1表示位置，{3}表示用第3个参数来填充，^表示居中，10表示占10个位置
    f_msg = msg.format("排名", "学校名称", "总分", '*')
    print(f_msg)


str_format1()
