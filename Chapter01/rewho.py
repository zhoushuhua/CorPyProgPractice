# -*- coding: cp936 -*-
# ������Ҫ��linuxϵͳ��ִ��
import re;
import os;

try:
    wf = os.popen("who", "r");
    for each_line in wf:
        print(re.split(r"\s\s+|\t", each_line.strip()));
except IOError as error:
    print("IOError error:" + str(error));
finally:
    if wf in locals():
        wf.close(); # �ر��ļ�
