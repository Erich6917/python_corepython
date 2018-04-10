# -*- coding: utf-8 -*-
# @Time    : 2018/2/7 
# @Author  : LIYUAN134
# @File    : fun_demo1.py
# @Commment: 
#


def avg(first, *rest):
    # 为了能让一个函数接受任意数量的位置参数，可以使用一个* 参数
    return (first + sum(rest)) / (1 + len(rest))


print avg(1, 2)
print avg(1, 2, 3, 4, 5)
