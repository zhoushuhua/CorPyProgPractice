# -*- coding: cp936 -*-
# ����ģ��
from socket import *

# �����ַ�Ͷ˿�
Host = "192.168.25.76"
Port = 21567
BufSize = 1024

Addr = (Host, Port)

while True:
    # ÿ�ζ���������
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    # ����
    tcpCliSock.connect(Addr)
    data = raw_input(">")
    if not data:
        break;
    tcpCliSock.send("%s\r\n" % data)
    # ���շ���
    r_data = tcpCliSock.recv(BufSize)
    if not r_data:
        break;
    print r_data.strip()
    tcpCliSock.close()
