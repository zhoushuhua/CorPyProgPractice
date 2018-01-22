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
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# 绑定主机信息
tcpSerSock.bind(Addr)
# 同时连接最大数
tcpSerSock.listen(5)

# 接收客户端连接
while True:
    print("waiting for connection……")
    tcpCliSock, addr = tcpSerSock.accept()
    print("…… connected from :", addr)
    while True:
        data = tcpCliSock.recv(BufSize)
        if not data:
            break;
        tcpCliSock.send(bytes("[%s] %s" %(ctime(), data), "utf-8") )
    # 关闭客户端连接
    tcpCliSock.close()
# 关闭套接字
tcpSerSock.close()
