# -*- coding: utf-8 -*-
# @Time    : 2017/12/19 
# @Author  : LIYUAN134
# @File    : SpiderLair.py
# @Commment: 爬虫多线程框架
#

import threading
import time

con = threading.Condition()
flag = False


class Box:
    def __init__(self):
        self.content = 0

    def setContent(self, content):
        self.content = content

    def getContent(self):
        return self.content


class Producer(threading.Thread):
    def __init__(self, box, name, count):
        super(Producer, self).__init__()
        self.box = box
        self.name = name
        self.count = count
        self.totalCount = count

    def run(self):
        global flag
        content = 0
        print "Producer " + self.name + " Start!\n"
        while self.count != 0:
            self.count = self.count - 1
            print "Producer acquiring the lock " + str(self.totalCount - self.count) + "th time!\n"
            con.acquire()
            print "Producer acquired the lock " + str(self.totalCount - self.count) + "th time!\n"
            if flag == True:
                print "Producer wait\n"
                con.wait()
            else:
                content = content + 1
                print "Producer put: " + str(content) + '\n'
                self.box.setContent(content)
                flag = True
                con.notify()
                con.release()
                time.sleep(1)
        print "The End of Producer !"


class Consumer(threading.Thread):
    def __init__(self, box, name, count):
        super(Consumer, self).__init__()
        self.box = box
        self.name = name
        self.count = count
        self.totalCount = count

    def run(self):
        global flag
        print "Consumer " + self.name + " Start!\n"
        while self.count != 0:
            self.count = self.count - 1
            print "Consumer acquiring the lock " + str(self.totalCount - self.count) + "th time!\n"
            con.acquire()
            print "Consumer acquired the lock " + str(self.totalCount - self.count) + "th time!\n"
            if flag == False:
                print "Consumer wait\n"
                con.wait()
            else:
                print "Consumer get: " + str(self.box.getContent()) + '\n'
                flag = False
                con.notify()
                con.release()
                time.sleep(1)
        print "The End of Consumer !"


if __name__ == '__main__':
    flag = False
    box = Box()
    p = Producer(box, "P", 10)
    c = Consumer(box, "C", 10)
    p.start()
    c.start()
