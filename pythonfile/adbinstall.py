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
                print(u"\n��װʧ�ܣ��϶���������İ������⣬����û��ǩ��\n" + r)
            else:
                print(u"\n��װ�ɹ���\n" + r)

# def command_line():
#     cmd_path = 'cmd /k cd /d c:\\Users\\Administrator\\'
#     os.system(cmd_path)

if __name__ == '__main__':
    print('dadad:%s', sys.argv)

    # command_line()
    while (True):
        print(u"\n������Ҫ��װ�İ���\n")
        path = input()
        if len(path):
            break
        else:
            print(u"\nû�а�װ������\n")
    adbInstall(path)


