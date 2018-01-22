# -*- coding: cp936 -*-
from twisted.internet import (protocol, reactor)
from time import ctime

PORT = 21567

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print "......connect from:", clnt

    def dataReceived(self, data):
        print "......receive data", data
        self.transport.write("[%s] %s" % (ctime(), data))

factory = protocol.Factory()
factory.protocol = TSServProtocol
print "wait for connect ......"
reactor.listenTCP(PORT, factory)
reactor.run()