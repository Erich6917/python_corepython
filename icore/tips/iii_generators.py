# -*- coding: utf-8 -*-
# @Time    : 2018/6/19 
# @Author  : ErichLee ErichLee@qq.com
# @File    : iii_generators.py
# @Comment : 
#            

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

'''
    本节主要总结Generators相关知识点
    在描述之前首先说下三个相关的概念
    Iterable
    Iterator
    Iteration
    
    Iterable
    iterable 是一个迭代器对象，它具有 __iter__() 方法并返回一个iterator ，
    或具有__getitem__()方法并可以从零开始的顺序索引（并且当索引不再有效时引发IndexError）。
    简而言之，iterable一个可以提供iterator的对象
    
    iterator
    iterator 是一个可迭代对象，它具有 next() (Python2)或 __next__() (Python3)方法。
    
    iteration
    iteration(迭代) 是在一行元素中一次取一个元素的过程
    当我们遍历访问一些元素时，就叫做iteration，就像它的名字一样，遍历它自己，是一个过程。
    
    
'''

'''
 举个例子,斐波那契数列的计算
'''


# list version
def fibon_base(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result


# generator version
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


# for x in fibon(1000):
#     print(x)

'''
    有两个版本可以用来计算
    fibon_base 和 fibon
    fibon方式基本上不用考虑性能问题
    但是fibon_base如果传入的值比较大会消耗大量的资源
'''


def generator_function():
    for i in range(3):
        yield i


def demo1():
    gen = generator_function()
    print(next(gen))
    # Output: 0
    print(next(gen))
    # Output: 1
    print(next(gen))
    # Output: 2
    print(next(gen))
    # Output: Traceback (most recent call last):
    #            File "<stdin>", line 1, in <module>
    #         StopIteration


def demo2():
    int_var = 1779
    iter(int_var)
    # Output: Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # TypeError: 'int' object is not iterable
    # This is because int is not iterable


def demo3():
    my_string = "Yasoob"
    my_iter = iter(my_string)
    print(next(my_iter))
    # Output: 'Y'


demo3()
