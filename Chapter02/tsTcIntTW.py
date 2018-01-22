# -*- coding: cp936 -*-
# 导入模块
from twisted.internet import protocol, reactor

Host = "192.168.25.76"
Port = 21567

class TWClntProtocol(protocol.Protocol):

    def sendData(self):
        data = raw_input(">")
        if not data:
            self.transport.loseConnection()
        else:
            print "......sending %s" % data
            self.transport.write(data)

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print "...... return data:", data
        self.sendData()

class TWClntFactory(protocol.ClientFactory):
    protocol = TWClntProtocol
    clientConnectionLost = clientConnectionFailed = \
        lambda self, connector, reason : reactor.stop()

reactor.connectTCP(Host, Port, TWClntFactory())
reactor.run()