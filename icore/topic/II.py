# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 
# @Author  : ErichLee ErichLee@qq.com
# @File    : ii_is_equal.py
# @Comment : 
#            

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def testFun():
    temp = [lambda x: i * x for i in range(4)]
    return temp


for everyLambda in testFun():
    print (everyLambda(2))
'''
最后发现原因竟是：Python 的闭包的后期绑定导致的 late binding，这意味着在闭包中的变量是在内部函数被调用的时候被查找。

所以结果是，当任何 testFun() 返回的函数被调用，在那时，i 的值是在它被调用时的周围作用域中查找，
到那时，无论哪个返回的函数被调用，for 循环都已经完成了，
i 最后的值是 3，因此，每个返回的函数 testFun 的值都是 3。
因此一个等于 2 的值被传递进以上代码，它们将返回一个值 6 （比如： 3 x 2）。
'''




