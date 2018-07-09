# -*- coding: utf-8 -*-
# @Time    : 2018/5/30 
# @Author  : ErichLee ErichLee@qq.com
# @File    : CallableDemo.py
# @Comment : 回调函数测试
#            

import sys
import functools

reload(sys)
sys.setdefaultencoding('utf-8')


# 1.装饰器
#
# 装饰器用来实现一种切面功能，即一些函数在调用前都必须实现的功能，
# 比如用户是否登录，用户是否有权限这类需求，都很容易由装饰器来实现。
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


# 给函数now定义了一个装饰器log,实现功能：在调用函数之前，打印出函数的名字
@log
def now():
    print('2015-3-25')


# now()


'''
    2.回调函数

    回调函数就是一个通过函数指针调用的函数。
    如果你把函数的指针（地址）作为参数传递给另一个函数，当这个指针被用来调用其所指向的函数时，我们就说这是回调函数。
    回调函数不是由该函数的实现方直接调用，而是在特定的事件或条件发生时由另外的一方调用的，用于对该事件或条件进行响应。
    
    个人理解的回调函数类似于这样一种情况，产品经理需要实现某种功能，需要找到开发，开发说我可以帮你写个函数实现这个功能，
    但是功能有点复杂，在不同的情况下需要传入不同的参数，这个参数是需要你来给我的。
    一般应用于对应某一事件触发的函数。
    比方要实现爬虫，我可以帮你写个爬虫函数，但是你首先得知道要爬虫网站的URL，大概就是这样一个意思。
    回调函数丰富了函数的调用方法，给开发带来很多方便。
'''


def test(num):
    for i in range(num):
        print 'hello,world'


def call(times, funcname):
    return funcname(times)


call(3, test)
