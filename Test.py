#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/13 19:15
# @Author  : Dicey
# @Site    : Soochow
# @File    : Test.py
# @Software: PyCharm

import itchat, time
import datetime as dt
from apscheduler.schedulers.background import BackgroundScheduler
import random

'''
测试文件
'''


greetList = ['test1', 'test2', 'test3', 'test4']

def tick():
    print('friendName()')
    users = itchat.search_friends(name='崔力辉')  # 你要找的ID名
    userName = users[0]['UserName']
    meetDate = dt.date(2018, 1, 14)  # 相识的日期
    now = dt.datetime.now()  # 现在的时间
    nowDate = dt.date.today()  # 今天的日期
    passDates = (nowDate - meetDate).days  # 认识的天数
    yourMess = random.sample(greetList, 1)[0]  # 你要发送的信息
    print(yourMess)

    itchat.send(yourMess, toUserName=userName)  # 发送信息
    nextTickTime = now + dt.timedelta(seconds=10)
    # print(str(dt.timedelta(seconds=10)))
    print('     现在的时间为:' + str(now), ';下一次发送的时间为:' + str(nextTickTime))
    # time.sleep(10)
    # nextTickTime = nextTickTime.strftime("%Y-%m-%d 00:00:00")
    print('**********')

    myScheduler(nextTickTime)


def myScheduler(runTime):
    print('myScheduel()')
    scheduler = BackgroundScheduler()
    print("     runTime:" + str(runTime))
    scheduler.add_job(tick, 'date', run_date=runTime)  # 在指定的时间只执行一次,基于日期的任务调度
    scheduler.start()


def testFun():
    '''
    1.登录个人微信
    在登录完成后获取当前时间
    然后设定下一个信息的时间为明天零点
    然后开启定时服务和微信服务
    :return:
    '''
    print('testFun')
    # 在命令行中展示二维码
    # itchat.auto_login(enableCmdQR=True)
    itchat.auto_login(hotReload=True)
    # 获取当前时间
    now = dt.datetime.now()
    # 以下二选一
    # nextTickTime = now + dt.timedelta(days=1)  # 现在时间加时间间隔为1天,即信息发送时间为明天的现在
    # nextTickTime = nextTickTime.strftime("%Y-%m-%d 00:00:00")  # 信息发生时间为明天零点
    nextTickTime = now
    myScheduler(nextTickTime)
    itchat.run()


if __name__ == '__main__':
    testFun()