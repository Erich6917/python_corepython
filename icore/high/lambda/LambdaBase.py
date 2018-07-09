# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 
# @Author  : ErichLee ErichLee@qq.com
# @File    : LambdaBase.py
# @Commment: 
#
from util.logger_util import *

"""
可以这样认为,lambda作为一个表达式，定义了一个匿名函数，上例的代码x为入口参数，x+1为函数体。
在这里lambda简化了函数定义的书写形式。是代码更为简洁，但是使用函数的定义方式更为直观，易理解。
Python中，也有几个定义好的全局函数方便使用的，filter, map, reduce。

"""


def lam_demo1():
    """
    lambda [arg1 [,arg2, ... argN]] : expression
    lambda函数可以在定义时直接被调用，比如
    """
    ljinfos("直接调用：")
    infos((lambda x, y: x - y)(3, 4))

    ljinfos("带if/else：")
    infos((lambda x, y: x if x < y else y)(1, 2))

    ljinfos("lambda嵌套")
    infos((lambda x: (lambda y: (lambda z: x + y + z)(1))(2))(3))

    ljinfos("递归：")
    fins = lambda n: 1 if n == 0 else n * fins(n - 1)
    infos(fins(3))
    f = lambda fins, n: 1 if n == 0 else n * fins(fins, n - 1)
    print f(f, 4)


def lam_demo2():
    """

    """
    print map(lambda x: x * x, [y for y in range(10)])

    a = [1, 2, 3]
    r = []
    for each in a:
        r.append(each + 1)
    print r
    print '两种写法相同'
    print map(lambda x: x + 1, [y for y in range(1, 4)])


lam_demo2()


def lam_msg():
    """
    可拼接名字输出
    """
    namelist = ['X-Man', 'spider-man', 'iron-man', 'super-man', 'pang-man', ]

    sqls = lambda group, remark: " update l_poi_table a set a.name =" + group + \
                                 " where (a.remark  is null or a.remark =" + remark + " ) " + \
                                 " and a.is_collected = -1"
    for name in namelist:
        print sqls(name, "REMARK_BY_" + name)


def run_demo1():
    funs = lambda x: x + 1

    print funs(1)
    print funs(2)


def run_demo2():
    from functools import reduce

    foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

    print (list(filter(lambda x: x % 3 == 0, foo)))
    # [18, 9, 24, 12, 27]

    print (list(map(lambda x: x * 2 + 10, foo)))
    # [14, 46, 28, 54, 44, 58, 26, 34, 64]

    print (reduce(lambda x, y: x + y, foo))
    # 139
    """
    上面例子中的map的作用，非常简单清晰。
    但是，Python是否非要使用lambda才能做到这样的简洁程度呢？
    在对象遍历处理方面，其实Python的for..in..if语法已经很强大，并且在易读上胜过了lambda。 　　
　　 比如上面map的例子，可以写成:print ([x * 2 + 10 for x in foo]) 非常的简洁，易懂。 　　
　　 filter的例子可以写成:print ([x for x in foo if x % 3 == 0]) 同样也是比lambda的方式更容易理解。
    """


def run_demo3():
    funcs = [lambda x: x + n for n in range(5)]
    for f in funcs:
        print f(0)

    print

    funcs = [lambda x, n=n: x + n for n in range(5)]
    for f in funcs:
        print f(0)
