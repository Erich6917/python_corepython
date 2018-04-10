# -*- coding: utf-8 -*-
# @Time    : 2017/12/29 
# @Author  : LIYUAN134
# @File    : process_demo2.py
# @Commment: 
#
from multiprocessing import Process, Lock
import time


class MyProcess(Process):
    def __init__(self, loop, lock):
        Process.__init__(self)
        self.loop = loop
        self.lock = lock

    def run(self):
        for count in range(self.loop):
            time.sleep(0.1)
            self.lock.acquire()
            print 'PID:' + str(self.pid) + ' Loop Count:' + str(count)
            self.lock.release()


if __name__ == '__main__':
    lock = Lock()
    for i in range(10, 25):
        p = MyProcess(i, lock)
        p.daemon = True  # 设置为守护进程
        p.start()
        p.join()  # 当所有进程执行完毕之后

    print 'The End'
