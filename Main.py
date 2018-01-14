#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/14 21:03
# @Author  : Dicey
# @Site    : Soochow
# @File    : Main.py
# @Software: PyCharm
'''
在微信中用来自动发送信息,不适合单身狗食用(所以说我为什么要写这个东西)
需求:
    1.定时发送信息
        定时是考虑是否随机时间段
    2.认识多少天(跟纪念日绑定)
    基于世卿大佬的代码
    3.天气
    4.讲段子
    5.(聊天机器人,doing...)
'''

import itchat
import datetime as dt
from apscheduler.schedulers.background import BackgroundScheduler
import random


class PDC(object):

    def __init__(self):
        '''
        构造方法
        :param herName: 你要聊天人的名字(备注)
        '''
        self.__scheduler = BackgroundScheduler()  # 调度器

        herName = input('她的名字(备注):\n')
        self.__herName = herName

        # 1.每天发送信息的时间(其他的动态效果啥的后来再加)

        self.__dailyHour, self.__dailyMinute, self.__dailySecond = map(int, input('发送每日信息的时间(格式 时:分:秒):').split(':'))
        # 2.每天要说的话

        # 3.纪念日与对应日子要说的话

        # 4.是否开启讲段子

        # 5.是否增加天气信息

    def forHer(self):
        '''
        你要做的事情
        :return:
        '''

    def showYourHeart(self):
        '''
        开始执行
        :return:
        '''

    def __dailyWhisper(self):
