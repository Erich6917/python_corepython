# -*- coding: utf-8 -*-
# @Time    : 2017/12/18 
# @Author  : LIYUAN134
# @File    : startQue.py
# @Commment: 
#            
import Queue


def demo1():
    q = Queue.Queue()

    for i in range(5):
        q.put(i)

    while not q.empty():
        print q.get(),
    print
    # 类似栈
    lifoQue = Queue.LifoQueue()
    for i in range(5):
        lifoQue.put(i)

    while not lifoQue.empty():
        print lifoQue.get(),


def test():
    demo1()


if __name__ == '__main__':
    test()
