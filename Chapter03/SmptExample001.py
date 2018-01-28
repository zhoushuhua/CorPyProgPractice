#! /usr/bin/python
# -*- coding: utf-8 -*-

# 邮件发送测试
from smtplib import SMTP

# 定义输入函数
def prompt(prompt):
    return raw_input(prompt).strip()

fromaddr = prompt("From: ")
toaddr = prompt("To:").split(",|\s")
print "Enter message, end with 'D(unix)' Or 'Z(windows)':"

msg = ("From:%s\r\nTo:%s\r\n\r\n" % (fromaddr, "," .join(toaddr)))
while True:
    try:
        line = raw_input()
    except EOFError as e:
        break
    if not line:
        break
    msg += line

print "Message length is " + repr(len(msg))

server = SMTP("localhost")
server.set_debuglevel(1)
server.sendmail(fromadd, toaddr, msg)
server.quit()