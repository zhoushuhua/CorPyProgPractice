#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
临界区加锁线程
"""

from atexit import register
from random import randrange
from threading import Thread, Lock, current_thread
from time import ctime,sleep

class CleanOutputSet(set):
    def __str__(self):
        return ",".join(self)

loops = (randrange(2,5) for x in range(randrange(3, 7)))
lock = Lock()
remaining = CleanOutputSet()

def loop(nesc):
    # 线程名称
    threadName = current_thread().name
    with lock:
        remaining.add(threadName)
        print("[%s] started %s" % (ctime(), threadName))
    # 睡眠
    sleep(nesc)
    with lock:
        remaining.remove(threadName)
        print("[%s] finished %s" % (ctime(), threadName))
        print("     (remaining:%s)" % (remaining or None))

@register
def atexit():
    print("all done at：", ctime())

def _main():
    for x in loops:
        Thread(target=loop, args = (x,)).start()

# 启动系统
if __name__ == "__main__":
    _main()