#! /usr/bin/python
# -*- coding: utf-8 -*-

from MyThread import MyThread
from time import ctime,sleep

loops = [4,2]

def loop(nloop, nsec):
    print "start loop", nloop, "at:", ctime()
    sleep(nsec)
    print "loop", nloop, "done at:", ctime()
    return nsec;

def main():
    print "start at:", ctime()
    threads = []
    nloops = range(len(loops))

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