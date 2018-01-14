#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/14 14:01
# @Author  : Dicey
# @Site    : Soochow
# @File    : SayHello.py
# @Software: PyCharm

import itchat
import datetime as dt
import random

greetList = ['test1', 'test2', 'test3', 'test4']


def tick(friendName):
    users = itchat.search_friends(name=friendName)  # 你要找的ID名
    userName = users[0]['UserName']
    meetDate = dt.date(2018, 1, 14)  # 相识的日期
    now = dt.datetime.now()  # 现在的时间
    nowDate = dt.date.today()  # 今天的日期
    passDates = (nowDate - meetDate).days  # 认识的天数
    yourMess = '今天是我们认识第'+str(passDates)+random.sample(greetList, 1)[0]  # 你要发送的信息
    print(yourMess)
    itchat.send(yourMess, toUserName=userName)  # 发送信息
    nextTickTime = now + dt.timedelta(days=1)
    nextTickTime = nextTickTime.strftime("%Y-%m-%d 00:00:00")

    my_scheduler(nextTickTime)



if __name__ == '__main__':
    print(random.sample(greetList, 1)[0])
