#coding=gbk
import re
import os
import subprocess
import sys


def adbInstall(path):
    cmd = 'adb install -r %s' % path
    print(cmd)
    s = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, encoding="utf-8")
    while subprocess.Popen.poll(s) is None:
        r = s.stdout.read()
        if r:
            print(r.strip())
            if r.strip() == 'Performing Streamed Install':
                print(u"\n安装失败：肯定是你拖入的包有问题，或者没有签名\n" + r)
            else:
                print(u"\n安装成功：\n" + r)

# def command_line():
#     cmd_path = 'cmd /k cd /d c:\\Users\\Administrator\\'
#     os.system(cmd_path)

if __name__ == '__main__':
    print('dadad:%s', sys.argv)

    # command_line()
    while (True):
        print(u"\n拖入你要安装的包：\n")
        path = input()
        if len(path):
            break
        else:
            print(u"\n没有安装包！！\n")
    adbInstall(path)


