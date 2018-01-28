#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import socket
import select

# 定义常量
HOST = "localhost"
PORT = 21567
BUFSIZE = 1024

# Listen ipt Message
INPUTS = []


# 定义主函数
def main():
	
    try:
        chatClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	chatClient.connect((HOST,PORT))
	INPUTS.append(chatClient)
	INPUTS.append(sys.stdin)
	
	while True:
	    print "1>>"
	    rlist, olist, elist = select.select(INPUTS, [], [])
	    for ipt in rlist:
	        if ipt == chatClient:
		    print ipt.recv(BUFSIZE)
		else:
		    idata = ipt.readline()
                    chatClient.send(idata)
    except socket.error as e:
        print "Error: Create Chat Client fail:", str(e)
        sys.exit(1)
    finally:
        chatClient.close()
    
#     try:
#         chatClient.connect((HOST, PORT))
#         ipt = [chatClient, sys.stdin]
#         readyInput, readyOutput, readyExceptions = select.select(ipt, [], [])
#         for indata in readyInput:
#             if indata == chatClient:
#                 data, addr = chatClient.recv(BUFSIZE)
#                 if data == 'q' or data == 'quit':
#                     chatClient.close()
#                 else:
#                     print "%s said: %s" % (addr, data)
#             else:
#                 message = ""
#                 if not message:
#                     message = raw_input()
#                 chatClient.send(message)
#             data = None
#     except socket.error as e:
#         print "Error: somthing wrong:", str(e)
#     # 关闭连接
#     chatClient.close()

# 程序入口
if __name__ == "__main__":
    main()
