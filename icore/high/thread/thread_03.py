# -*- coding: utf-8 -*-
# @Time    : 2017/12/29 
# @Author  : LIYUAN134
# @File    : thread_03.py
# @Commment: 
#            
# !/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time

import icore.high.thread

exitFlag = 0


class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print "Starting " + self.name
        threadlock.acquire()
        print_time(self.name, self.counter, 5)
        threadlock.release()
        print "Exiting " + self.name


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            icore.high.thread.exit()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1


threadlock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启线程
thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)
for t in threads:
    t.join()
print "Exiting Main Thread"
