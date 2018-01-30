#! /usr/bin/python
# -*- coding: utf-8 -*-

from cStringIO import StringIO
from imaplib import IMAP4_SSL
from platform import python_version
from poplib import POP3_SSL
from smtplib import SMTP

# 验证python的版本
release = python_version()
if release < "2.6.3":
    SMTP_SSL = None;
else:
    from smtplib import SMTP_SSL  # fixed 2.6.3

#from secret import *

who = "%s@gmial.com" % "zhoushuhua721"
from_ = who
to_ = who
MAILBOX = "zhoushuhua721@qq.com"
PASSWD = "&aixiaoli*466453"

heads = [
    "From:%s" % from_,
    "To:%s" % to_,
    "Subject: Test SMTP send via 587/TLS"
]

body = [
    "Hello",
    "World"
]

msg = "\r\n\r\n".join(("\r\n".join(heads), "\r\n".join(body)))

def getSubject(msg, defaultSubject="No Subject Line"):
    """
    getSubject(Msg) iterator over "msg"  looking for
    Subject line; return if found otherwise "default"
    :param msg:
    :param defaultSubject:
    :return:
    """
    for line in msg:
        if line[:8] == "Subject:":
            return line.rstrip()
    return defaultSubject

print "***  Doing SMTP send via TLS  ***"
s = SMTP("smtp.gmail.com", 587)
if release < "2.6":
    s.ehlo()
s.starttls()
if release < "2.5":
    s.ehlo()
s.login(MAILBOX, PASSWD)
s.send(from_, to_, msg)
s.quit()

print " TLS mail sent!"

# print  "***  Doing PoP Recv  ***"
# s = POP3_SSL("pop.gmail.com", 995)
# s.user(MAILBOX)
# s.pass_(PASSWD)
# rv, msg, sz = s.retr(s.stat()[0])
# s.quit()
# line = getSubject(msg)
# print "received msg via POP: %r" % line
# body = body.replace("587/TLS", "465/TLS")

if SMTP_SSL:
    print "***  Doing SMTP send via SSL  ***"
    s = SMTP_SSL("smtp.gmail.com", 465)
    s.login(MAILBOX, PASSWD)
    s.send(from_, to_, msg)
    s.quit()
    print "SSL mial sent"

print "***  Doing IMAP recv  ***"
s = IMAP4_SSL("imap.gmail.com", 993)
s.login(MAILBOX, PASSWD)
rsp, msgs = s.select("INBOX", True)
rsp, data = s.fetch(msg[0], "(RFC822)")
line = getSubject(StringIO(data[0][1]))
s.close()
s.logout()
print "   received msg via IMAP : %r" % line