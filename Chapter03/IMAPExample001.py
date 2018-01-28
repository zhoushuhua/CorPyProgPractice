#! /usr/bin/python
# -*- coding: utf-8 -*-

from imaplib import IMAP4

# 初始化
imap = IMAP4("imap.python.is.cool")
imap.login("wesley", "password")

rsp, msgs = s=imap.slect("INBOX", True)
res, data = imap.fetch(msgs[0], "(RFC822)")
for line in data[0][1].splitlines()[:5]:
    print line

rsp, data = imap.fetch("98", "(body)")
print data[0]

rsp, data = imap.fetch("98", "(body[header])")
print data[0][1][:45]

rsp, data = imap.search(None, "SEEN")

rsp, data = imap.fetch("98:100", "(BODY[HEADER])")
print data[0][1][:45]

imap.close()
imap.logout()