#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import socket
import select

# 定义常量
HOST = ""
PORT = 21567
BUFSIZE = 1024

# defined sock list
SOCK_LIST = []
Addr_Dict = {}

# defined
chatServer = None

# 定义主函数
def main():
    try:
        # 创建Server
	global chatServer
        chatServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        chatServer.bind((HOST, PORT))
        chatServer.listen(10)
	SOCK_LIST.append(chatServer)
    except socket.error as e:
        print "Creating Socket Server error:", str(e)
        sys.exit(1)

    try:
	# listen socket
	while True:
	    readyInput, readyOutput, readyException = select.select(SOCK_LIST, [], [])
            for sk in readyInput:
		if sk == chatServer:
		    chatClient, Addr = chatServer.accept()
		    print "connect from:", Addr
		    SOCK_LIST.append(chatClient)
		    Addr_Dict[chatClient] = Addr
		    distributeMsg(chatClient, "Client <%s> connected" % str(Addr))
		else:
		    # client socket
		    data = sk.recv(BUFSIZE)
		    data = "<%s> said: %s" % (str(Addr_Dict[sk]), data)
		    print data
		    distributeMsg(sk, data)
    except socket.error as e:
        print "Something is wrong:%s" % str(e)

# distribute msg
def distributeMsg(sock, msg):
    for sk in SOCK_LIST:
	if sk != chatServer and sk != sock:
	    try:
	        sk.send(msg)
	    except:
		print "maybe client is closed"
		SOCK_LIST.remove(sk)
		Addr_Dict.remove(sk)

if __name__ == "__main__":
    main()
