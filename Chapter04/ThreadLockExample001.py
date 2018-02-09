#! /usr/bin/python
# -*- coding: utf-8 -*-

import thread
from time import ctime,sleep

loops = [4,2]

def loop(nloop, nsec, lock):
    print "start loop", nloop, "at:", ctime()
    sleep(nsec)
    print "loop", nloop, "done at:", ctime()
    lock.release()

def main():
    print "start at:", ctime()
    locks = []
    nloops = range(len(loops))

    # 获取锁对象
    # for i in nloops:
    #     lock = thread.allocate_lock()
    #     lock.acquire()
    #     locks.append(lock)

    for i in nloops:
        lock = thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
        thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked(): pass
    print "all done at:", ctime()

# 启动系统
if __name__ == "__main__":
    main()