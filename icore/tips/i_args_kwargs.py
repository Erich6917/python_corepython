# -*- coding: utf-8 -*-
# @Time    : 2018/6/11
# @Author  : ErichLee ErichLee@qq.com
# @File    : i_args_kwargs.py
# @Comment : 参数*args and **kwargs问题讨论
#            资料参考 http://book.pythontips.com/en/latest/args_and_kwargs.html

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from loggerUtil import *

'''
 Example 1
 构造一个可接受任意数量参数的函数。

'''


def test_args(f_arg, *argv):
    infos("first:", f_arg)
    for arg in argv:
        infos("rest:", arg)


test_args('yasoob', 'python', 'eggs', 'test')

'''
 Example 2.1
 为了接受任意数量的关键字参数，使用一个以** 开头的参数

'''
println()


def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} welcome {1}".format(key, value))


# greet_me('jam', 'jame') # ERROR
# greet_me(host='jame', guest='jemmy')
greet_me(host='jame', guest='jemmy', other='others')

'''
 Example 2.2
 **参数举例

'''
println()


def make_element(name, value, **attrs):
    import html
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value))
    infos(element)


make_element('item', 'Albatross', size='large', quantity=6)

'''
一个* 参数只能出现在函数定义中最后一个位置参数后面，而**参数只能出现在
最后一个参数。有一点要注意的是，在* 参数后面仍然可以定义其他参数。
def a(x, *args, y):
    pass
def b(x, *args, y, **kwargs):
    pass

It really depends on what your requirements are. 
The most common use case is when making function decorators (discussed in another chapter). 
Moreover it can be used in monkey patching as well. 
Monkey patching means modifying some code at runtime. 
Consider that you have a class with a function called get_info which calls an API and returns the response data. 
If we want to test it we can replace the API call with some test data
'''
