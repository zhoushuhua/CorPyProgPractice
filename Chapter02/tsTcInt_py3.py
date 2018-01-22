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
    data = input(">")
    if not data:
        break;
    tcpCliSock.send(bytes(data, "utf-8"))
    # 接收返回
    r_data = tcpCliSock.recv(BufSize)
    if not r_data:
        break;
    print(bytes.decode(r_data, "utf-8"))

tcpCliSock.close()
