#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/14 21:27
# @Author  : Dicey
# @Site    : Soochow
# @File    : InputTest.py
# @Software: PyCharm

import datetime
import itchat, time
# import datetime as dt
from apscheduler.schedulers.background import BackgroundScheduler
import random
from datetime import datetime, timedelta


def tick2():
    print('tick2')


def tick():
    print('tick1')


def myScheduler(runTime):
    print('myScheduel()')
    scheduler = BackgroundScheduler()
    print("     runTime:" + str(runTime))
    scheduler.add_job(tick, 'date', run_date=runTime + dt.timedelta(seconds=10))  # 在指定的时间只执行一次,基于日期的任务调度
    scheduler.add_job(tick2, 'date', run_date=runTime + dt.timedelta(seconds=5))  # 在指定的时间只执行一次,基于日期的任务调度

    scheduler.start()


if __name__ == '__main__':
    # myScheduler(dt.datetime.now())
    h, m, s = map(int, input().split(':'))

    now = datetime.now()
    print(now)
    delta = timedelta(hours=h, minutes=m, seconds=s)
    print(delta)
    nextTime = datetime.strptime(now.strftime("%Y-%m-%d 00:00:00"), '%Y-%m-%d %H:%M:%S')
    final = (nextTime) + delta
    print(nextTime)
    print(final)
