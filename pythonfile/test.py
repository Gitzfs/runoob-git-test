# -*- coding: gbk -*-

import os
import re
from time import sleep
os_path = os.getcwd()
'''�ж��ֻ���Ŀ¼���Ƿ����iar����log'''
# �ж��Ƿ�װadb������systemִ�гɹ�����0,�񷵻�1
cmd = 'adb version 2> error.txt'
a = os.system(cmd)
if a == 0:
    print("adb��������", a)
else:
    print("adb�����쳣", a)

# ����豸���Ƿ����jar��
jar_name = 'monkey.jar'
jar_name2 = 'framework.jar'
ls = 'adb shell ls /sdcard'
adb_ls = os.popen(ls)
data = adb_ls.read()
print(data)
if jar_name in data and jar_name2 in data:
    print("�����豸�м�⵽��{}��{}".format(jar_name, jar_name2))
else:
    print("δ���豸�м�⵽��{}��{}".format(jar_name, jar_name2))

# ��ȡִ��monkey��ı�����־������
log_txt = 'crash-dump.log'
# log_txt = 'monkey_log.txt'

if log_txt in data:
    pull_log = f'adb pull /sdcard/crash-dump.log {os_path}'
    os.popen(pull_log)
    print("��־�ѱ��浽", os_path)
else:
    print("δ���豸���ҵ���", log_txt)