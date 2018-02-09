#! /usr/bin/python
# -*- coding: utf-8 -*-

import threading
from time import ctime,sleep

loops = [4,2]

def loop(nloop, nsec):
    print "start loop", nloop, "at:", ctime()
    sleep(nsec)
    print "loop", nloop, "done at:", ctime()

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
        thread = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(thread)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()
    print "all done at:", ctime()

# 启动系统
if __name__ == "__main__":
    main()