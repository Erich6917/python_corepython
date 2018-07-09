# -*- coding: utf-8 -*-
# @Time    : 2017/9/18 
# @Author  : LIYUAN134
# @Site    : 
# @File    : gc.py
# @Comment : 继承测试
#


class P1:  # (object): # parent class 1 父类1

    def foo(self):
        print 'called P1-foo()'


class P2:  # (object): # parent class 2 父类2

    def foo(self):
        print 'called P2-foo()'

    def bar(self):
        print 'called P2-bar()'


class C1(P1, P2):  # child 1 der. from P1, P2 #子类1，从P1，P2 派生


    pass


class C2(P1, P2):  # child 2 der. from P1, P2 #子类2，从P1，P2 派生


    def bar(self):
        print 'called C2-bar()'


class GC(C1, C2):  # define grandchild class #定义子孙类

    pass  # derived from C1 and C2 #从C1，C2 派生


gc = GC()
# test1
# 当调用foo()时，它首先在当前类(GC)中查找。如果没找到，就向上查找最亲的父类，C1。查找
# 未遂，就继续沿树上访到父类P1，foo()被找到。
gc.foo()
gc.bar()

# test2
# 现在，你可能在想，“我更愿意调用C2 的bar()方法，因为它在继承树上和我更亲近些，这样才
# 会更合适。”在这种情况下，你当然还可以使用它，但你必须调用它的合法的全名，采用典型的非绑
# 定方式去调用，并且提供一个合法的实例：

C2.bar(gc)