# -*- coding: cp936 -*-
# 程序需要在linux系统中执行
import re;
import os;
from distutils.log import warn as printf

try:
    wf = os.popen("who", "r");
    for each_line in wf:
        printf(re.split(r"\s\s+|\t", each_line.strip()));
except IOError as error:
    print("IOError error:" + str(error));
finally:
    if wf in locals():
        wf.close(); # 关闭文件
