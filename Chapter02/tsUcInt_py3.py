# -*- coding: cp936 -*-
# ����ģ��
from socket import *

# ��������
Host = "192.168.25.76"
# ����˿ں�
Port = 21567
# ������ջ�����
BufSize = 1024

Addr = (Host, Port)
try:
    udpClient = socket(AF_INET, SOCK_DGRAM)

    # ѭ����������
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
