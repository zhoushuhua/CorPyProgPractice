# -*- coding: cp936 -*-
# ������Ҫ��linuxϵͳ��ִ��
import re;
import os;

try:
    wf = os.popen("tasklist/nh", "r");
    for each_line in wf:
        print(re.findall(r"([\w.]+(?: [\w.]+)*)\s\s+(\d+) (\w+)\s\s+(\d+)\s\s+([\d,]+ K)", each_line.strip()));
except IOError as error:
    print("IOError error:" + str(error));
finally:
    if wf in locals():
        wf.close(); # �ر��ļ�
