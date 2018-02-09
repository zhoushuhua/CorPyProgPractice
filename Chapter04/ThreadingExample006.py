#! /usr/bin/python
# -*- coding: utf-8 -*-

from MyThread import MyThread
from time import ctime,sleep

loops = [4,2]

def fib(x):
    sleep(0.005)
    if x < 2: return 1
    return (fib(x - 2) + fib(x - 1))

def fac(x):
    sleep(0.1)
    if x < 2: return 1
    return (x * fac(x - 1))

def sum(x):
    sleep(0.1)
    if x < 2: return 1
    return (x + sum(x - 1))

funcs = [fib, fac, sum]
n = 20

def main():
    nfuncs = range(len(funcs))

    print "*** Single Thread ***"
    for i in nfuncs:
        print "starting", funcs[i].__name__, "at:", ctime()
        print funcs[i](n)
        print funcs[i].__name__, " finished", "at:", ctime()

    print "*** Multiple Thread ***"
    threads = []
    for i in nfuncs:
        threads.append(MyThread(func=funcs[i], args = (n,), name = funcs[i].__name__))

    for i in nfuncs:
        print "starting", funcs[i].__name__, "at:", ctime()
        threads[i].start()
    for i in nfuncs:
        threads[i].join()
        print funcs[i].__name__, " finished", "at:", ctime()

if __name__ == "__main__":
    main()