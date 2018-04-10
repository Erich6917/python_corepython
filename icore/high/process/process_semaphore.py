# -*- coding: utf-8 -*-
# @Time    : 2017/12/29 
# @Author  : LIYUAN134
# @File    : process_semaphore.py
# @Commment: 
#            
from multiprocessing import Process, Semaphore, Lock, Queue
import time
from random import random
from multiprocessing import Process, Semaphore, Lock, Queue
import time



buffer = Queue(10)
empty = Semaphore(3)
full = Semaphore(1)
lock = Lock()

class Consumer(Process):

    def run(self):
        global buffer, empty, full, lock
        while True:
            print 'loop c'
            full.acquire()
            lock.acquire()
            buffer.d
            buffer.get()
            print('Consumer pop an element')
            time.sleep(1)
            lock.release()
            empty.release()


class Producer(Process):
    def run(self):
        global buffer, empty, full, lock
        while True:
            print 'loop p'
            empty.acquire()
            lock.acquire()
            buffer.put(1)
            print('Producer append an element')
            time.sleep(1)
            lock.release()
            full.release()


if __name__ == '__main__':
    p = Producer()
    c = Consumer()
    p.daemon = c.daemon = True
    p.start()
    c.start()
    p.join()
    c.join()
    print 'Ended!'