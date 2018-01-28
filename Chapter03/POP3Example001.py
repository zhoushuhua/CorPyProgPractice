#! /usr/bin/python
# -*- coding: utf-8 -*-

import getpass, poplib

m = poplib.POP3("pop.python.is.cool")
m.user(getpass.getuser())
m.pass_(getpass.getpass())
numMessage = len(m.list()[1])
for i in range(numMessage):
    for j in m.retr(i+1)[1]:
        print j