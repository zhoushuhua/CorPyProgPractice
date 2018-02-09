#! /usr/bin/python
# -*- coding: utf-8 -*-

import threading

class MyThread(threading.Thread):
    def __init__(self, func, args, name=""):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    # 获取结果
    def getReslut(self):
        return self.res;

    # 执行函数
    def run(self):
        self.res = self.func(*self.args)