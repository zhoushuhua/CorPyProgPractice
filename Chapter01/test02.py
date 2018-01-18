# -*- coding: cp936 -*-
import re

data = "Wed Mar 15 16:25:00 2017::osfti@onhga.gov::1489566300-5-5";
##patt = "^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)";

# 匹配
##m = re.match(patt, data)
##if m is not None : print(m.group())
##if m is not None : print(m.group(1))
##if m is not None : print(m.groups())

##patt = "^(\w{3})"
##m = re.match(patt, data)
##if m is not None : print(m.group())

##patt = "^(\w){3}"
##m = re.match(patt, data)
##if m is not None : print(m.group())

##patt = "\d+-\d+-\d+"
##m = re.search(patt, data)
##if m is not None : print(m.group())

##patt = ".+\d+-\d+-\d+"
##m = re.match(patt, data)
##if m is not None : print(m.group())

##patt = ".+(\d+-\d+-\d+)"
##m = re.match(patt, data)
##if m is not None : print(m.group(1))

##patt = ".+?(\d+-\d+-\d+)"
##m = re.match(patt, data)
##if m is not None : print(m.group(1))

patt = "-(\d+)-"
m = re.search(patt, data)
if m is not None : print(m.group(1))
