# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 
# @Author  : ErichLee ErichLee@qq.com
# @File    : ii_is_equal.py
# @Comment : python中is 和 ==的区别
#            

import sys

from loggerUtil import *

reload(sys)
sys.setdefaultencoding('utf-8')


def show1():
    a = 10000000
    b = 10000000

    a = 'ssfdsf'
    b = 'ssfdsf'
    infos('a>id is {0} , b>id is {1}'.format(id(a), id(b)))
    infos('a==b > {0}'.format(a == b))
    infos('a is b > {0} '.format(a is b))


# show1()


'''
    is" 是用来比较 a 和 b 是不是指向同一个内存单元，而"=="是用来比较 a 和 b指向的内存单元中的值是不是相等
    以下是关于python类的
    is 和 ==
    同样的is表示 内存地址是否相同，==表示 地址所指向的值是否相等   
    对应于java要重写equal和hashcode方法来说
    python要重写__eq__方式，来控制类是否指向同一个
    
    以下为demo测试 

'''


class Pformer(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name \
               and self.age == other.age


p1 = Pformer('Joe', '23')
p2 = Pformer('Joe', '23')

infos('p1>id is {0} , p2>id is {1}'.format(id(p1), id(p2)))
infos('p1==p2 > {0}'.format(p1 == p2))
infos('p1 is p2 > {0} '.format(p1 is p2))
