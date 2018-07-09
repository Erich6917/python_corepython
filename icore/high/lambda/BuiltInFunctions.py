# -*- coding: utf-8 -*-
# @Time    : 2018/4/17
# @Author  : ErichLee ErichLee@qq.com
# @File    : BuiltInFunctions.py
# @Commment: python 内建函数集合
#

import sys
from util.logger_util import *

reload(sys)
sys.setdefaultencoding('utf-8')


def py_input():
    """
    Python3.x 中 input() 函数接受一个标准输入数据，返回为 string 类型。
    Python2.x 中 input() 相等于 eval(raw_input(prompt)) ，用来获取控制台的输入。
                 raw_input() 将所有输入作为字符串看待，返回字符串类型。
    而 input() 在对待纯数字输入时具有自己的特性，它返回所输入的数字的类型（ int, float ）。
    """
    infos("Py2.x input函数只接受数字类型")
    ins = input("仅可输入数字类型:")
    infos("type:", type(ins))

    msgs = raw_input("可输入任意类型的：")
    infos("msgs:", msgs)



def is_odd(n):
    return n % 2 == 0


def py_filters():
    # 内置函数-filter
    # 以下是 filter() 方法的语法:
    # filter(function, iterable)
    # function -- 判断函数。
    # iterable -- 可迭代对象。
    init_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # or range(1,11)
    newlist = filter(is_odd, init_arr)
    print newlist

    # 与lambda组合
    # Python built-in function
    print filter(lambda x: x % 2 == 0, init_arr)


def py_map():
    # map() 会根据提供的函数对指定序列做映射。
    #
    # 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
    #
    # map(function, iterable, ...)

    infos("一个序列元素处理：")
    print map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数

    infos("两个序列元素处理：对应位置相加：")
    print map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])

    infos("如果函数有多个参数, 但每个参数的序列元素数量不一样, 会根据最少元素的序列进行：仅在python3支持")
    # listx = [1, 2, 3, 4, 5, 6, 7]  # 7 个元素
    # listy = [2, 3, 4, 5, 6, 7]  # 6 个元素
    # listz = [100, 100, 100, 100]  # 4 个元素
    # print map(lambda x, y, z: x ** 2 + y + z, listx, listy, listz)
    ss = open("aa.txt", 'a+')
    print >> ss, "nihao"
    ss.close()


def py_all():
    """
    all(iterable)
    参数--iterable -- 元组或列表。
    返回值
    --如果iterable的所有元素不为0、''、False或者iterable为空，all(iterable)返回True，否则返回False；
    注意：空元组、空列表返回值为True，这里要特别注意。
    """
    infos("注意函数的局限性，将数字0，False，空字符串加入了判断")
    ljinfos("all(['a', 'b', 'c', 'd'])", all(['a', 'b', 'c', 'd']))  # 列表list，元素都不为空或0
    ljinfos("all(['a', 'b', '', 'd']) ", all(['a', 'b', '', 'd']))  # 列表list，存在一个为空的元素
    ljinfos("all([0, 1，2, 3])", all([0, 1, 2, 3]))  # 列表list，存在一个为0的元素
    ljinfos("all(('a', 'b', 'c', 'd'))", all(('a', 'b', 'c', 'd')))  # 元组tuple，元素都不为空或0
    ljinfos("all(('a', 'b', '', 'd')) ", all(('a', 'b', '', 'd')))  # 元组tuple，存在一个为空的元素
    ljinfos("all((0, 1，2, 3)) ", all((0, 1, 2, 3)))  # 元组tuple，存在一个为0的元素
    ljinfos("all([])", all([]))  # 空列表
    ljinfos("all(()) ", all(()))  # 空元组


def py_important():
    """
    常用的一些内置函数
    """
    msg = "runoob"
    sarr = [1, 2, 3, 4, 5]
    infos("msg=", msg)
    infos("sarr=", sarr)
    ljinfos("1.len()判断长度 len(sarr) > ", len(msg))
    ljinfos("2.type()判断类型 type(msg)", type(msg))
    ljinfos("3.range()整数数组 API显示list of integers：", "range(start, stop[, step]) ", )
    ljinfos(" >1-9的数组>range(10)", range(10))
    ljinfos(" >1-9的数组>range(1,10)", range(1, 10))
    ljinfos(" >1-9的数组>range(1,10,1)", range(1, 10, 1))
    ljinfos("4.list() 方法用于将元组转换为列表")
    ljinfos(" > list([1, 2, 3])", list([1, 2, 3]))
    ljinfos(" > list(['back', 'home'])", list(['back', 'home']))


def py_numbers():
    """
    数字类型  二进制十进制八进制待整理
    """
    print float(-123.6)
    print long(2.1)
