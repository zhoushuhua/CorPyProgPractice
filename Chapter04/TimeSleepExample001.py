#! /usr/bin/python
# -*- coding: utf-8 -*-

from time import ctime,sleep

# 定义循环体
def loop1():
    print "start loop1 time:" + str(ctime())
    sleep(4)
    print "done loop1 time:" + str(ctime())

# 定义循环体
def loop2():
    print "start loop2 time:" + str(ctime())
    sleep(2)
    print "done loop2 time:" + str(ctime())

# 定义主函数
def main():
    print "start main time:" + str(ctime())
    loop1()
    loop2()
    sleep(6)
    print "done main time:" + str(ctime())

# 启动系统
if __name__ == "__main__":
    main()