#! /usr/bin/python
# -*- coding: utf-8 -*-

import threading
from time import ctime,sleep

loops = [4,2]

def loop(nloop, nsec):
    print "start loop", nloop, "at:", ctime()
    sleep(nsec)
    print "loop", nloop, "done at:", ctime()
    return nsec;

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

def main():
    print "start at:", ctime()
    threads = []
    nloops = range(len(loops))

    # 获取锁对象
    # for i in nloops:
    #     lock = thread.allocate_lock()
    #     lock.acquire()
    #     locks.append(lock)

    for i in nloops:
        thread = MyThread(loop, (i, loops[i]))
        threads.append(thread)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    for i in nloops:
        print "thread ret",threads[i].res;
    print "all done at:", ctime()

# 启动系统
if __name__ == "__main__":
    main()