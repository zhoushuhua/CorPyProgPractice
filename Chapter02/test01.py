# -*- coding: cp936 -*-
import socket

# 创建有连接的tcp套接字
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 创建无连接的udp套接字
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
