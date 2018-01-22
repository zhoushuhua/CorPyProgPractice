# -*- coding: cp936 -*-
# 导入模块
from socket import *
from time import ctime

# 定义主机
Host = ""
# 定义端口号
Port = 21567
# 定义接收缓冲区
BufSize = 1024

Addr = (Host, Port)
try:
    udpServer = socket(AF_INET, SOCK_DGRAM)
    udpServer.bind(Addr)

    # 循环接收数据
    while True:
        print("waiting for messge……")
        data, addr = udpServer.recvfrom(BufSize)
        if not data:
            break;
        print("receive Data:", data)
        udpServer.sendto(bytes("[%s] %s" % (ctime(), data), "utf-8"), addr)
        # 输出接收到的数据
        print ("…… received from and returned to：", addr)
except EOFError as error:
    print("EOFError:" + str(error))
finally:
    if udpServer in locals():
        udpServer.close()
