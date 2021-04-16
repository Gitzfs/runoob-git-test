# -*- coding:utf-8 -*-
import os


# 判断目标是否存在,file or folder
a = os.path.exists('adb')
print("判断目标是否存在:", a)

# 判断目标是否目录
b = os.path.isdir('directory')
print("判断目标是否目录:", b)

# 判断目标是否文件
c = os.path.isfile('file')
print("判断目标是否文件:", c)

# 判断目标文件夹是否存在，如果不存在则创建一个文件夹
if os.path.exists('adb'):
    print("文件夹已存在！")
else:
    os.mkdir('adb')
    print("文件夹已经创建！")

# 打开一个文件如果不存在则创建一个
file = open('test.txt', 'w')
# 关闭文件
file.close()

# 删除文件夹
os.rmdir('adb')