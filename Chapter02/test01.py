# -*- coding: cp936 -*-
import socket

# ���������ӵ�tcp�׽���
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ���������ӵ�udp�׽���
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
