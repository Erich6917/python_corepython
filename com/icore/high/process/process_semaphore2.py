# -*- coding: utf-8 -*-
# @Time    : 2018/1/4
# @Author  : LIYUAN134
# @File    : process_semaphore2.py
# @Commment:
#
import multiprocessing
import time


def worker(s, i):
    s.acquire()
    print(multiprocessing.current_process().name + "acquire");
    time.sleep(i)
    print(multiprocessing.current_process().name + "release\n");
    s.release()


if __name__ == '__main__':
    se = multiprocessing.Semaphore(2)
    for ii in range(50):
        p = multiprocessing.Process(target=worker, args=(se, ii))
        p.start()
