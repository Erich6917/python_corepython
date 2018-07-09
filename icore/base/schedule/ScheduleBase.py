# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 
# @Author  : ErichLee ErichLee@qq.com
# @File    : ScheduleBase.py
# @Commment: 
#            
from datetime import datetime
import time
import sys
from apscheduler.schedulers.background import BackgroundScheduler
import os

reload(sys)
sys.setdefaultencoding('utf-8')


def tick():
    print('Tick! The time is: %s' % datetime.now())


def start_demo1():
    scheduler = BackgroundScheduler()
    scheduler.add_job(tick, 'interval', seconds=3)  # 间隔3秒钟执行一次
    scheduler.start()  # 这里的调度任务是独立的一个线程
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)  # 其他任务是独立的线程执行
            print('sleep!')
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
        print('Exit The Job!')


def start_schedule():
    """
    非阻塞调度，在指定的时间执行一次
    """
    scheduler = BackgroundScheduler()
    scheduler.add_job(tick, 'date', run_date='2018-04-26 10:39:05')  # 在指定的时间，只执行一次
    scheduler.start()  # 这里的调度任务是独立的一个线程
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))


def start_schedule2():
    """
    非阻塞的方式，采用cron的方式执行
    """
    scheduler = BackgroundScheduler()
    scheduler.add_job(tick, 'cron', day_of_week='3', second='*/5')
    scheduler.start()
    '''
    year (int|str) – 4-digit year
    month (int|str) – month (1-12)
    day (int|str) – day of the (1-31)
    week (int|str) – ISO week (1-53)
    day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
    hour (int|str) – hour (0-23)
    minute (int|str) – minute (0-59)
    second (int|str) – second (0-59)

    start_date (datetime|str) – earliest possible date/time to trigger on (inclusive)
    end_date (datetime|str) – latest possible date/time to trigger on (inclusive)
    timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone)

    *    any    Fire on every value
    */a    any    Fire every a values, starting from the minimum
    a-b    any    Fire on any value within the a-b range (a must be smaller than b)
    a-b/c    any    Fire every c values within the a-b range
    xth y    day    Fire on the x -th occurrence of weekday y within the month
    last x    day    Fire on the last occurrence of weekday x within the month
    last    day    Fire on the last day within the month
    x,y,z    any    Fire on any matching expression; can combine any number of any of the above expressions
    '''


def start_schedule3():
    """
    阻塞的方式，间隔3秒执行一次
    """
    scheduler = BackgroundScheduler()
    scheduler.add_job(tick, 'interval', seconds=3)
    scheduler.start()


def start_sleep():
    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)  # 其他任务是独立的线程执行
            print('sleep!')
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
        print('Exit The Job!')


def main_start():
    # start_schedule() # 非阻塞调度，在指定的时间执行一次
    start_schedule2()  # 启动策略
    start_schedule3()  # 阻塞的方式，间隔3秒执行一次
    start_sleep()


if __name__ == '__main__':
    # start_demo1()
    main_start()
