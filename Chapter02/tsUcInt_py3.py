# -*- coding: cp936 -*-
# 导入模块
from socket import *

# 定义主机
Host = "192.168.25.76"
# 定义端口号
Port = 21567
# 定义接收缓冲区
BufSize = 1024

Addr = (Host, Port)
try:
    udpClient = socket(AF_INET, SOCK_DGRAM)

    # 循环接收数据
    while True:
        data = input(">")
        if not data:
            break;
        udpClient.sendto(bytes(data, "utf-8"), Addr)
        r_data,Addr = udpClient.recvfrom(BufSize)
        if not data:
            break;
        print("return:", r_data)
except EOFError as error:
    print("EOFError:" + str(error))
finally:
    if udpClient in locals():
        udpClient.close()
