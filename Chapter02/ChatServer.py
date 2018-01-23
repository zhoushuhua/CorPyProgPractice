#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import socket
import select

# 定义常量
HOST = "localhost"
PORT = 21567
BUFSIZE = 2014

# 定义主函数
def main():
    try:
        # 创建Server
        chatServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print "Creating Socket Server error:", str(e)
        sys.exit(1)

    try:
        chatServer.bind((HOST, PORT))
        chatServer.listen(1)
        ipt = [chatServer, sys.stdin]

        while True:
            print "waiting connection……"
            chatClient, addr = chatServer.accept()
            print "connection from:", addr
            ipt.append(chatClient)
            while True:
                readyInput, readyOutput, readyException = select.select(ipt, [], [])
                for indata in readyInput:
                    if indata == chatClient:
                        data = chatClient.recv(BUFSIZE)
                        if data == "q" or data == "quit":
                            chatClient.close()
                        else:
                            print "%s said: %s" % (addr, data)
                    else:
                        message = ""
                        while not message:
                            message = raw_input()
                        chatClient.send(message)
                    data = None
    except socket.error as e:
        print "Something is wrong:%s", str(e)

if __name__ == "__main__":
    main()