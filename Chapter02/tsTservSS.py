# -*- coding: cp936 -*-
# ����ģ��
from SocketServer import (TCPServer as TCP,
    StreamRequestHandler as SRH)
from time import ctime

# ���崦������¼���
class MyRequestHandler(SRH):

    # �����¼�������
    def handle(self):
        print "����connected from:", self.client_address
        self.wfile.write("[%s] %s" % (ctime(), self.rfile.readline()))

# ������������Ϣ
Host = ""
Port = 21567
Addr = (Host, Port)

ts = TCP(Addr, MyRequestHandler)
print "waiting for connection����"
ts.serve_forever()
