# -*- coding: cp936 -*-
# 导入模块
from socket import *

# 定义地址和端口
Host = "192.168.25.76"
Port = 21567
BufSize = 1024

Addr = (Host, Port)
tcpCliSock = socket(AF_INET, SOCK_STREAM)
# 连接
tcpCliSock.connect(Addr)

while True:
    data = raw_input(">")
    if not data:
        break;
    tcpCliSock.send(data)
    # 接收返回
    r_data = tcpCliSock.recv(BufSize)
    if not r_data:
        break;
    print r_data

tcpCliSock.close()
