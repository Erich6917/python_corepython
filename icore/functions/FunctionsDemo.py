# -*- coding: utf-8 -*-
# @Time    : 2018/5/30
# @Author  : ErichLee ErichLee@qq.com
# @File    : FunctionsDemo.py
# @Comments: python函数测试
#

import sys
import html

reload(sys)
sys.setdefaultencoding('utf-8')

# 1.可接受任意数量参数的函数
# Writing Functions That Accept Any Number of
# Arguments
"""
    参数传递
    *  -> tuple
    ** -> dict
    
    一个* 参数只能出现在函数定义中最后一个位置参数后面，
    而**参数只能出现在最后一个参数。
    有一点要注意的是，在* 参数后面仍然可以定义其他参数。

"""


# 任意数量的位置参数，可以使用一个* 参数
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


# print avg(1, 2, 3)
# print avg(1, 2, 3, 4, 5)

# 任意数量的关键字参数，使用一个以** 开头的参数

def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(name=name, attrs=attr_str, value=html.escape(value))
    return element


# print make_element('item', 'Albatross', size='large', quantity=6)
# print make_element('p', '<spam>')

