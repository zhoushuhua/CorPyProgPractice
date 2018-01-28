#! /usr/bin/python
# -*- coding: utf-8 -*-

from smtplib import SMTP
from poplib import POP3
from time import sleep


# 定义常量
SMTPSVR = "smtp.python.is.cool"
POPSVR = "pop.python.is.cool"

who = "wesley@python.is.cool"
body = """
From:%(who)s
To:%(who)s
Subject:test msg

Hello World
""" % {"who" : who}

# 定义发送邮件
def sendMsg():
    stp = SMTP(SMTPSVR)
    errs = stp.send(who, who, body)
    stp.quit()
    assert len(errs) == 0, errs

def downloadMsg():
    pop = POP3(POPSVR)
    pop.user("wesley")
    pop.pass_("pass")
    rsp, msg, siz = pop.retr(pop.stat()[0])
    # Sting header and compare to orig msg
    seq = msg.index("")
    recvBody = msg[seq + 1:]

if __name__ == "__main__":
    sendMsg()
    sleep(10)
    downloadMsg()