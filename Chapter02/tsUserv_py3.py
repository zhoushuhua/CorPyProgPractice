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
try:
    udpServer = socket(AF_INET, SOCK_DGRAM)
    udpServer.bind(Addr)

    # ѭ����������
    while True:
        print("waiting for messge����")
        data, addr = udpServer.recvfrom(BufSize)
        if not data:
            break;
        print("receive Data:", data)
        udpServer.sendto(bytes("[%s] %s" % (ctime(), data), "utf-8"), addr)
        # ������յ�������
        print ("���� received from and returned to��", addr)
except EOFError as error:
    print("EOFError:" + str(error))
finally:
    if udpServer in locals():
        udpServer.close()
