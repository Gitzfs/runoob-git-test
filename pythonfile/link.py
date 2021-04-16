import os
import re
from time import sleep

# print("当前执行目录:", os.getcwd())
#adb_name = 'Android Debug Bridge'
def run_path():
    # python脚本启动路径
    path = os.getcwd()
    return path

def adbtools_path(run_path):
    # adb工具路径
    path = run_path + '\\adbtools'
    return path

def isadb():
    # 检测是否配置adb环境
    run_adb = "adb version 2> error_log.txt"
    adb_type = os.system(run_adb)
    sleep(2)
    if adb_type != 0:
        print('未配置 adb环境')
    return adb_type


def adb_config(run_pash):
    # 在C盘根目录中 放置 adb工具包
    adbpath = 'C:\\adbtools'
    cp_adb = 'xcopy {}\\adbtools C:\\adbtools /I/Q/E/y'.format(run_pash)
    print("正在拷贝adb工具，请稍后")
    os.system(cp_adb + ' 2>> error_log.txt')
    sleep(1)
    print('adb工具拷贝成功')
    print('请手动设置 adb环境变量 \nadb工具路径为：%s' % adbpath)

def adb_link():
    # 连接设备，并提取多设备 设备名
    str_init = ' '
    devices_info = os.popen('adb devices').readlines()
    for i in range(len(devices_info)):
        str_init += devices_info[i]
    devices_info = re.findall('\n(.+?)\t', str_init, re.S)
    return devices_info

def toadb():
    # 切换至工具箱中adb目录
    run = run_path()
    path = adbtools_path(run)
    os.chdir(path)
    os.system('adb version')
if __name__ == '__main__':
    toadb()
