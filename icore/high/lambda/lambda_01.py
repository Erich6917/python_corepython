# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 
# @Author  : LIYUAN134
# @File    : lambda_01.py
# @Commment: 
#

"""
可以这样认为,lambda作为一个表达式，定义了一个匿名函数，上例的代码x为入口参数，x+1为函数体。
在这里lambda简化了函数定义的书写形式。是代码更为简洁，但是使用函数的定义方式更为直观，易理解。
Python中，也有几个定义好的全局函数方便使用的，filter, map, reduce。

"""


def run_demo1():
    fun_d1 = lambda x: x + 1
    print fun_d1(1)
    print fun_d1(2)
    # # 以上lambda等同于以下函数
    # def func(x):
    #     return (x + 1)


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
