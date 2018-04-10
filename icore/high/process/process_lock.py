# -*- coding: utf-8 -*-
# @Time    : 2018/1/4 
# @Author  : LIYUAN134
# @File    : process_lock.py
# @Commment: lock使用
#
from multiprocessing import Pool, Process, Lock
import datetime
import sys


def workder_with(lock, f):
    with lock:
        fs = open(f, 'a+')
        fs.write('===========================  ')
        fs.write(str(datetime.datetime.now()))
        fs.write('\n')
        n = 10
        while n > 0:
            fs.write('Locked acquired via with \n')
            n -= 1
        fs.close()


def worker_no_with(lock, f):
    lock.acquire()
    try:
        fs = open(f, 'a+')
        fs.write('VVVVVVVVVVVVVVVVVVVVVVVVVVV ')
        fs.write(str(datetime.datetime.now()))
        fs.write('\n')
        n = 10
        while n > 0:
            fs.write('Locked acquired directly \n')
            n -= 1
    finally:
        lock.release()


if __name__ == '__main__':
    print datetime.datetime.now()
    lock = Lock()
    f = 'file.txt'
    w = Process(target=workder_with, args=(lock, f))
    nw = Process(target=worker_no_with, args=(lock, f))
    w.start()
    nw.start()

    print 'The End'
