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
        print threading.current_thread().getName(), 'music'
        # for i in range(3):
        #     print i, "I was listening to music. %s. %s:" % (name, self.ctime())

    def move(self, name):
        print threading.current_thread().getName(), 'move'
        # for i in range(6):
        #     print i, " I was watching CCTV-5. %s. %s:" % (name, self.ctime())

    def player(self, name):
        r = name.split('.')[1]
        if r == 'mp3':
            self.music(name)
        else:
            if r == 'avi':
                self.move(name)
            else:
                print 'error: The format is not recognized!'


if __name__ == '__main__':
    tr = training()
    list = ['民族最旋风.mp3', '爱情公寓.avi']
    threads = []
    files = range(100)
    # files = range(len(list))
    for i in files:
        t = threading.Thread(target=tr.player, args=(list[i % 2],))
        t.setDaemon(True)
        t.start()
        t.join()
    # (注意:join()方法的位置是在for循环外的，也就是说必须等待for循环里的两个进程都结束后，才去执行主进程。)

    print "all over %s" % tr.ctime()
