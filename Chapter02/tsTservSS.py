# -*- coding: cp936 -*-
# 导入模块
from SocketServer import (TCPServer as TCP,
    StreamRequestHandler as SRH)
from time import ctime

# 定义处理接收事件类
class MyRequestHandler(SRH):

    # 定义事件处理函数
    def handle(self):
        print "……connected from:", self.client_address
        self.wfile.write("[%s] %s" % (ctime(), self.rfile.readline()))

# 定义主机等信息
Host = ""
Port = 21567
Addr = (Host, Port)

ts = TCP(Addr, MyRequestHandler)
print "waiting for connection……"
ts.serve_forever()
