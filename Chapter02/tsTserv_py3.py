# -*- coding: cp936 -*-
# ����ģ��
from socket import *
from time import ctime

# ��������
Host = ""
# ����˿ں�
Port = 21567
# ������ջ�����
BufSize = 1024

Addr = (Host, Port)
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# ��������Ϣ
tcpSerSock.bind(Addr)
# ͬʱ���������
tcpSerSock.listen(5)

# ���տͻ�������
while True:
    print("waiting for connection����")
    tcpCliSock, addr = tcpSerSock.accept()
    print("���� connected from :", addr)
    while True:
        data = tcpCliSock.recv(BufSize)
        if not data:
            break;
        tcpCliSock.send(bytes("[%s] %s" %(ctime(), data), "utf-8") )
    # �رտͻ�������
    tcpCliSock.close()
# �ر��׽���
tcpSerSock.close()
