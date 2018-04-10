# -*- coding: utf-8 -*-
# @Time    : 2017/12/29 
# @Author  : LIYUAN134
# @File    : process_start.py
# @Commment: python进程
#            
import multiprocessing
import thread
import time

'''
    # https://thief.one/2016/11/24/Multiprocessing-Process/
    利用multiprocessing.Process对象可以创建一个进程，该Process对象与Thread对象的用法相同，
    也有start(), run(), join()等方法。
    Process类适合简单的进程创建，如需资源共享可以结合multiprocessing.Queue使用；
    如果想要控制进程数量，则建议使用进程池Pool类。
    
    Process介绍
    
    构造方法：
    
    Process([group [, target [, name [, args [, kwargs]]]]])
    group: 线程组，目前还没有实现，库引用中提示必须是None；
    target: 要执行的方法；
    name: 进程名；
    args/kwargs: 要传入方法的参数。
    实例方法：
    
    is_alive()：返回进程是否在运行。
    join([timeout])：阻塞当前上下文环境的进程程，直到调用此方法的进程终止或到达指定的timeout（可选参数）。
    start()：进程准备就绪，等待CPU调度。
    run()：strat()调用run方法，如果实例进程时未制定传入target，这star执行t默认run()方法。
    terminate()：不管任务是否完成，立即停止工作进程。
    属性：
    
    authkey
    daemon：和线程的setDeamon功能一样（将父进程设置为守护进程，当父进程结束时，子进程也结束）。
    exitcode(进程在运行时为None、如果为–N，表示被信号N结束）。
    name：进程名字。
    pid：进程号。


'''


# 创建多进程的两种方法
#
# Process类中，可以使用两种方法创建子进程。
# 说明：通过继承Process类，修改run函数代码。

# 使用Process类继承创建子进程
class MyProcess(multiprocessing.Process):
    def __init__(self, arg):
        super(MyProcess, self).__init__()
        self.arg = arg

    def run(self):
        time.sleep(3)
        print 'mask', self.arg


def process(num):
    time.sleep(3)
    print 'Process:', num


if __name__ == '__main__':
    for ii in range(10):
        p = MyProcess(ii)
        p.start()

    for ii in range(10):
        p.join()


def test_demo1():
    # 最简单的创建Process的过程如上所示，target传入函数名，args是函数的参数，是元组的形式，
    # 如果只有一个参数，那就是长度为1的元组。
    # 然后调用start()方法即可启动多个进程了。
    for i in range(5):
        p = multiprocessing.Process(target=process, args=(i,))
        p.start()


def test_demo2():
    #     可以通过 cpu_count() 方法还有 active_children() 方法获取当前机器的 CPU 核心数量以及得到目前所有的运行的进程。


    for i in range(5):
        p = multiprocessing.Process(target=process, args=(i,))
        p.start()

    print('CPU number:' + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print('Child process name: ' + p.name + ' id: ' + str(p.pid))

    print('Process Ended')


def test_demo3():
    """
    ==TEST1==============================
    p.start()
    output:
        end
        Process: 33
        只调用start方法，先输出end，后输出process

    ==TEST2==============================
    p.daemon = True
    p.start()
    output:
        end 设置守候线程为TRUE,只输出end，程序结束

    ==TEST3==============================
    p.start()
    p.join()
    output:
        Process: 33
        end 正确输出，p.daemon使用默认值

    ==TEST3==============================
    p.daemon = True
    p.start()
    p.join()
    output:
        Process: 33
        end  推荐写法
    """
    p = multiprocessing.Process(target=process, args=(33,))
    # p.daemon = True
    p.start()
    p.join()
    print 'end'


'''
    进程的创建 
    例demo1，调用 multiprocessing.Process 启动即可
    demo2，没有daemon 属性 和调用join，导致main走完，直接关闭线程


'''

# if __name__ == '__main__':
#     # test_demo1()
#     # test_demo2()
#     test_demo3()
