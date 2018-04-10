# -*- coding: utf-8 -*-
# @Time    : 2018/1/11 
# @Author  : LIYUAN134
# @File    : num.py
# @Commment: 
#
from loggerUtil import printLine


def demo_1():
    """
        四舍五入
    """
    print round(1.23, 1)
    print round(1.27, 1)
    print round(-1.27, 1)
    print round(-1.22, 1)
    print round(1.25361, 3)

    printLine()
    # 传给round() 函数的ndigits 参数可以是负数，这种情况下，舍入运算会作用在十位、百位、千位等上面
    a = 1627731
    print round(a, -1)
    print round(a, -2)

    printLine()
    # 不要将舍入和格式化输出搞混淆
    x = 1.23456
    print format(x, '0.2f')
    print format(x, '0.3f')

    printLine()
    # 同样，不要试着去舍入浮点值来” 修正” 表面上看起来正确的问题
    a = 2.1
    b = 4.2
    c = a + b
    print c
    print round(c, 2)

    printLine()



demo_1()
