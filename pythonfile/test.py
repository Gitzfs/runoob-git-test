# -*- coding: gbk -*-

import os
import re
from time import sleep
os_path = os.getcwd()
'''判断手机根目录下是否存在iar包和log'''
# 判断是否安装adb环境，system执行成功返回0,否返回1
cmd = 'adb version 2> error.txt'
a = os.system(cmd)
if a == 0:
    print("adb环境正常", a)
else:
    print("adb环境异常", a)

# 检查设备中是否存在jar包
jar_name = 'monkey.jar'
jar_name2 = 'framework.jar'
ls = 'adb shell ls /sdcard'
adb_ls = os.popen(ls)
data = adb_ls.read()
print(data)
if jar_name in data and jar_name2 in data:
    print("已在设备中检测到：{}、{}".format(jar_name, jar_name2))
else:
    print("未在设备中检测到：{}、{}".format(jar_name, jar_name2))

# 获取执行monkey后的崩溃日志到电脑
log_txt = 'crash-dump.log'
# log_txt = 'monkey_log.txt'

if log_txt in data:
    pull_log = f'adb pull /sdcard/crash-dump.log {os_path}'
    os.popen(pull_log)
    print("日志已保存到", os_path)
else:
    print("未在设备中找到：", log_txt)