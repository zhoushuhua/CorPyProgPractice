# -*- coding: cp936 -*-
# 程序需要在linux系统中执行
import re;
import os;

try:
    with os.popen("who", "r") as wf:
        print(re.split(r"\s\s+|\t", each_line.strip()));
except IOError as error:
    print("IOError error:" + str(error));
finally:
    if wf in locals():
        wf.close(); # 关闭文件
