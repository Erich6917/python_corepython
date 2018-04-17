# -*- coding: utf-8 -*-
# @Time    : 2018/1/11 
# @Author  : ErichLee ErichLee@qq.com
# @File    : NumbersBase.py
# @Commment: 数字类型基础
#
from util.loggerUtil import *
from decimal import Decimal
import random


def num_round():
    """
        数字类型的四舍五入
    """
    ljinfos("round(1.23, 1)", round(1.23, 1))
    ljinfos("round(1.27, 1)", round(1.27, 1))
    ljinfos("round(-1.27, 1)", round(-1.27, 1))
    ljinfos("round(-1.22, 1)", round(-1.22, 1))
    ljinfos("round(1.25361, 3)", round(1.25361, 3))
    printLine()

    infos("传给round() 函数的ndigits 参数可以是负数，这种情况下，舍入运算会作用在十位、百位、千位等上面")
    a = 1627731
    ljinfos("round(a, -1)", round(a, -1))
    ljinfos("round(a, -2)", round(a, -2))
    printLine()

    infos("不要将舍入和格式化输出搞混淆,如果只是输出一定宽度的数字没必要调用round函数，直接用format格式化即可")
    x = 1.23456
    ljinfos("format(x, '0.2f')", format(x, '0.2f'))
    ljinfos("format(x, '0.3f')", format(x, '0.3f'))
    printLine()


def num_deciamls():
    """
        小数类型计算
    """
    a = Decimal('4.2')
    b = Decimal('2.1')
    infos("浮点类型的计算，使用decimal模块，增加精度")
    infos((a + b) == Decimal('6.3'))


def num_format():
    """
        数字格式化输出
    """
    infos("数字格式化输出 x = 1234.56789")
    x = 1234.56789
    ljinfos("format(x, '0.2f')", format(x, '0.2f'))
    ljinfos("format(x, '>20.1f')", format(x, '>10.1f'))
    ljinfos("format(x, '<10.1f')", format(x, '<10.1f'))
    ljinfos("format(x, '^10.1f')", format(x, '^10.1f'))
    ljinfos("format(x, ',')", format(x, ','))
    ljinfos("format(x, '0,.1f')", format(x, '0,.1f'))

    ljinfos("format(x, 'e')", format(x, 'e'))
    ljinfos("format(x, '0.2E')", format(x, '0.2E'))


def num_fractions():
    """
        分数运算
    """
    from fractions import Fraction
    a = Fraction(5, 4)
    b = Fraction(7, 16)
    infos(a + b)

    c = a * b
    infos("c >", (a * b))
    ljinfos("c.numerator", c.numerator)
    ljinfos("c.denominator", c.denominator)


def num_random():
    """
        随机函数
    """
    values = [1, 2, 3, 4, 5, 6]

    infos("每次单个随机数 random.choice(values)")
    for i in range(1, 5):
        infos(i, '随机数 > ', random.choice(values))
    printLine()

    infos("每次多个随机数 random.sample(values, 2)")
    for i in range(1, 5):
        infos(i, '随机数 > ', random.sample(values, 2))
    printLine()

    infos("打乱元素顺序： random.shuffle(values)")
    for i in range(1, 3):
        random.shuffle(values)
        infos(values)
    printLine()

    infos("随机数的生成 random.randint(0,10)")
    for i in range(1, 5):
        infos(random.randint(0, 10))
