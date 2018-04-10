# -*- coding: utf-8 -*-
# @Time    : 2018/1/2 
# @Author  : LIYUAN134
# @File    : process_pool.py
# @Commment: 
#
from multiprocessing import Pool, Process
import time

'''
    Multiprocessing.Pool可以提供指定数量的进程供用户调用，当有新的请求提交到pool中时，
    如果池还没有满，那么就会创建一个新的进程用来执行该请求；
    但如果池中的进程数已经达到规定最大值，那么该请求就会等待，直到池中有进程结束，才会创建新的进程来执行它。
    在共享资源时，只能使用Multiprocessing.Manager类，而不能使用Queue或者Array。

    Pool介绍

    用途

    Pool类用于需要执行的目标很多，而手动限制进程数量又太繁琐时，如果目标少且不用控制进程数量则可以用Process类。

    构造方法

    Pool([processes[, initializer[, initargs[, maxtasksperchild[, context]]]]])
    processes ：使用的工作进程的数量，如果processes是None那么使用 os.cpu_count()返回的数量。
    initializer： 如果initializer是None，那么每一个工作进程在开始的时候会调用initializer(*initargs)。
    maxtasksperchild：工作进程退出之前可以完成的任务数，完成后用一个新的工作进程来替代原进程，来让闲置的资源被释放。maxtasksperchild默认是None，意味着只要Pool存在工作进程就会一直存活。
    context: 用在制定工作进程启动时的上下文，一般使用 multiprocessing.Pool() 或者一个context对象的Pool()方法来创建一个池，两种方法都适当的设置了context。

    实例方法

    apply_async(func[, args[, kwds[, callback]]]) 它是非阻塞。
    apply(func[, args[, kwds]])是阻塞的。
    close() 关闭pool，使其不在接受新的任务。
    terminate() 关闭pool，结束工作进程，不在处理未完成的任务。
    join() 主进程阻塞，等待子进程的退出， join方法要在close或terminate之后使用。


'''


def func(msg):
    print "msg:", msg
    time.sleep(3)
    print "end", msg
    return "done", msg


# 使用进程池（非阻塞）
# if __name__ == "__main__":
#     pool = Pool(processes=3)
#     for i in xrange(66):
#         msg = "hello %d" % (i)
#         pool.apply_async(func, (msg,))  # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
#
#     print "Mark~ Mark~ Mark ~~~~~~~~~~~~~~~~~~~~~~"
#
#     pool.close()
#     pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
#
#     print "Sub-process(es) done."

'''
    apply_async(func[, args[, kwds[, callback]]]) 它是非阻塞，apply(func[, args[, kwds]])是阻塞的（理解区别，看例1例2结果区别）
    close()    关闭pool，使其不在接受新的任务。
    terminate()    结束工作进程，不在处理未完成的任务。
    join()    主进程阻塞，等待子进程的退出， join方法要在close或terminate之后使用。

'''
# 使用进程池（阻塞）
# if __name__ == "__main__":
#     pool = Pool(processes=3)
#     for i in xrange(4):
#         msg = "hello %d" % (i)
#         pool.apply(func, (msg,))  # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
#
#     print "Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~"
#     pool.close()
#     pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
#     print "Sub-process(es) done."

# 使用进程池（阻塞）

# if __name__ == "__main__":
#     pool = Pool(processes=3)
#     for i in xrange(5):
#         msg = "hello %d" % (i)
#         pool.apply(func, (msg,))  # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
#
#     print "Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~"
#     pool.close()
#     pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
#     print "Sub-process(es) done."

if __name__ == "__main__":
    pool = Pool(processes=4)
    result = []
    for i in xrange(11):
        msg = "hello %d" % (i)
        result.append(pool.apply_async(func, (msg,)))
    pool.close()
    pool.join()
    for res in result:
        print ":::", res.get()
    print "Sub-process(es) done."
