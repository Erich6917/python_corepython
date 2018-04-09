# -*- coding: utf-8 -*-
# @Time    : 2017/12/13
# @Author  : LIYUAN134
# @File    : unicode.py
# @Commment:
#

# Python的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号，列表使用方括号。
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

def func_getmsg():
    a = 1
    b = '33'
    return a, b


def func_getlist():
    a = [1, 3, 4, 5, 6]
    b = 4
    return a, b


def test_getmsg():
    a, b = func_getmsg()
    print a
    print b

    la, lb = func_getlist()
    print la
    print lb


def demo_create():
    tup1 = ('physics', 'chemistry', 1997, 2000)
    tup2 = (1, 2, 3, 4, 5)
    tup3 = "a", "b", "c", "d"
    print tup1
    print tup2
    print tup3

    print



if __name__ == '__main__':
    demo_create()
