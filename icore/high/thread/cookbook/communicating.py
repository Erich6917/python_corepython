# -*- coding: utf-8 -*-
# @Time    : 2018/1/1 
# @Author  : LIYUAN134
# @File    : communicating.py
# @Commment: 线程之间的交互
#
from Queue import Queue
from threading import Thread
import random


# A thread that produces data
def producer(out_q):
    while True:
        # Produce some data
        out_q.put(random.randint(10, 100))


# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()
        print data
        # Process the data


# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()
