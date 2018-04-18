# coding=utf-8
'''
Created on 2017年11月28日

@author: Administrator
'''
import datetime
import threading


class training():
    def ctime(self):
        nowTime = datetime.datetime.now()
        currTime = datetime.datetime.strftime(nowTime, '%Y-%m-%d %H:%M:%S')
        return currTime

    def music(self, name):
        for i in range(3):
            print i, "I was listening to music. %s. %s:" % (name, self.ctime())

    def move(self, name):
        for i in range(6):
            print i, " I was watching CCTV-5. %s. %s:" % (name, self.ctime())


if __name__ == '__main__':
    tr = training()
    threads = []
    t1 = threading.Thread(target=tr.music, args=(u'民族最旋風',))
    threads.append(t1)
    #     t2 = threading.Thread(target=tr.move,args=(u'愛情公寓'))
    #     threads.append(t2)
    t2 = threading.Thread(target=tr.move, args=(u'愛情公寓',))
    threads.append(t2)

    for t in threads:
        #         setDaemon(True)将线程声明为守护线程，必须在start() 方法调用之前设置，
        #          如果不设置为守护线程程序会被无限挂起。子线程启动后，父线程也继续执行下去，
        #            当父线程执行完最后一条语句print "all over %s" %ctime()后，
        #            没有等待子线程，直接就退出了，同时子线程也一同结束。
        t.setDaemon(True)
        t.start()
        t.join()
    # (注意:join()方法的位置是在for循环外的，也就是说必须等待for循环里的两个进程都结束后，才去执行主进程。)

    print "all over %s" % tr.ctime()
