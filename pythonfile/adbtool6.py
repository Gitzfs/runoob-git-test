import sys
import os
import re
import time
import urllib.request
import qrcode
from urllib import error
from PIL import Image

# 获取的是脚本目录，不包含文件名
print(r"当前执行目录:%s\ADB_tool5.exe" % os.getcwd())
os_path = os.getcwd()

lists = ("\n1、传输文件到手机\n\n2、清除当前运行APP数据(支持多台)\n\n3、安装应用(支持多台)\n\n4、查看当前运行APP包名\n\n"
         "5、截图\n\n6、卸载当前运行APP(支持多台)\n\n7、执行Monkey(支持多台)\n\n"
         "8、诸葛万年历Monkey(支持多台)\n\n9、重启设备(支持多台)\n\n10、清除诸葛万年历数据\n\n11、获取日志(支持多台)\n\n12、执行maxim(支持多台)\n\n13、自动下载安装APK\n\n0、结束\n")
list = list(range(0, 14))
Executing = str("正在执行:")
complete = str("执行结束。")

def get_deviceid():
    # 获取设备多台设备号列表
    str_init = ' '
    all_info = os.popen('adb devices').readlines()
    for i in range(len(all_info)):
        str_init += all_info[i]
    all_info = re.findall('\n(.+?)\t', str_init, re.S)
    return all_info

devices_list = get_deviceid()

def adb_push(push_path):
    #  传文件到手机
    print(Executing)
    os.popen(r'adb -s ' + devices_list[0] + r' push %s /sdcard/' % push_path).readlines()
    print(complete)
    # return push

def adb_install(path):
    # 安装apk
    for i in devices_list:
        cmd = r'adb -s ' + i + r' install -r %s' % path
        print("正在执行:", cmd, "\n正在后台安装请等待...")
        install = os.popen(cmd)
        context = install.read()
        for line in context.splitlines():
            success = line
            print(line)
            if success == "Success":
                print("安装成功:", success)
            else:
                print("安装失败:", success)

def adb_screen():
    # 截屏
    pathss = os.getcwd()
    print(pathss)
    cmd = r"adb shell screencap -p /sdcard/screen.png"
    print(Executing, cmd)
    screen = os.popen(cmd)
    time.sleep(3)
    cmd2 = fr"adb pull /sdcard/screen.png  {pathss}\screenshots\screen.png"
    pus = os.popen(cmd2)
    time.sleep(1)
    print(fr"已保存到:{pathss}\screenshots\screen.png")
    return screen, pus

def adb_pm():
    # 清除缓存
    # comm = str(input("请输入包名:"))
    for i in devices_list:
        cmd = r'adb -s ' + i + ' shell dumpsys window | findstr mCurrentFocus'
        com = os.popen(cmd)
        context = com.read()
        for line in context.splitlines():
            # print(line)
            regx = "u0 (.*?)/"
            result = re.findall(regx, line)
        for p in result:
            cmd = r'adb -s ' + i + ' shell pm clear %s' % p
            print('正在执行:', cmd)
            pm = os.popen(cmd)
            print(f'缓存已清除，Package:{p} \n')
def adb_uninstall(Package):
    # 卸载应用
    for i in devices_list:
        print(Package)
        if Package == '':
            # 如未获取到包名则重新获取当前在运行的包名
            cmd = r'adb -s ' + i + ' shell dumpsys window | findstr mCurrentFocus'
            com = os.popen(cmd)
            context = com.read()
            for line in context.splitlines():
                regx = "u0 (.*?)/"
                result = re.findall(regx, line)
                Package = result[0]
            cmd = r'adb -s ' + i + ' uninstall %s ' % Package
            print("正在卸载:", cmd)
            os.popen(cmd)
            print("卸载完成！\n")
            Package = ''
        else:
            cmd = r'adb -s ' + i + ' uninstall %s ' % Package
            print("正在卸载:", cmd)
            os.popen(cmd)
            print("卸载完成！\n")

def adb_com():
    # 查看包名
    for i in devices_list:
        cmd = r'adb -s ' + i + ' shell dumpsys window | findstr mCurrentFocus'
        print("正在执行:", cmd)
        com = os.popen(cmd)
        context = com.read()
        for line in context.splitlines():
            # print(line)
            regx = "u0 (.*?)/"
            result = re.findall(regx, line)
            result2 = result[0]
            print("当前包名:", result2, "\n")
            com.close()

def adb_reboot():
    # 重启设备
    for i in devices_list:
        cmd = 'adb -s ' + i + ' reboot'
        print("正在执行:", cmd)
        os.popen(cmd)
def adb_monkey():
    apk = str(input("输入包名(默认当前APP):"))
    # 如果apk为None则重新获取包名,否则获取用户输入的包名
    if apk == '':
        for i in devices_list:
            cmd = r'adb -s ' + i + ' shell dumpsys window | findstr mCurrentFocus'
            com = os.popen(cmd)
            context = com.read()
            for line in context.splitlines():
                # print(line)
                regx = "u0 (.*?)/"
                result = re.findall(regx, line)
                apk = result[0]
            com.close()
            print("未输入包名，默认包名:", apk)
            break
    else:
        print("输入的包名：", apk)
    # 限制执行步数只能输入int类型
    times = input("输入要执行的事件数（默认90000000）：")
    if not re.findall('^[0-9]+$', times):
        # 输入的数值不符合规则，给一个默认值90000000
        times = 90000000
        print("默认事件数：", times)
    else:
        print("输入的事件数：", times)
    # 对多个设备执行monkey命令
    for i in devices_list:
        cmd2 = 'adb -s ' + i + ' shell monkey -p ' + apk + '  --pct-syskeys 0 --pct-anyevent  0 --ignore-crashes --ignore-timeouts --throttle 120 -v -v -v %s' % times
        print("正在执行:", cmd2)
        os.popen(cmd2)

def adb_monkeys():
    for i in devices_list:
        cmd = 'adb -s ' + i + ' shell monkey -p com.geek.luck.calendar.app --pct-syskeys 0 --pct-anyevent  0 --ignore-crashes --ignore-timeouts --throttle 120 -v -v -v 90000000'
        print("正在执行:", cmd)
        os.popen(cmd)
def adb_cache():
    for i in devices_list:
        cmd = 'adb -s ' + i + ' shell pm clear com.geek.luck.calendar.app'
        print("正在执行:", cmd)
        os.popen(cmd)
        print(complete)
def adb_logcat():
    pathss = os.getcwd()
    time.sleep(0.5)
    for i in devices_list:
        cmd = 'adb -s ' + i + fr' shell dumpsys dropbox --print >%s\log\crash{i}.txt' % pathss
        print("正在执行:", cmd)
        os.popen(cmd)
        print(f'日志已保存到:%s\crash{i}.txt \n' % pathss)
def adb_maxim(pushjar):
    apk = [] # 初始化定义列表
    apk.append(str(input("输入包名(默认当前APP):")))
    # 如果apk为None则重新获取包名,否则获取用户输入的包名
    if apk[0] == '':
        apk = [] # 初始化
        for i in devices_list:
            pushmonkey = rf'adb -s {i} push {pushjar}\monkey.jar /sdcard/'
            pushwork = rf'adb -s {i} push {pushjar}\framework.jar /sdcard/'
            print(pushmonkey)
            os.popen(pushmonkey)
            print(pushwork)
            os.popen(pushwork)
            time.sleep(1)
            cmd = r'adb -s ' + i + ' shell dumpsys window | findstr mCurrentFocus'
            com = os.popen(cmd)
            context = com.read()
            for line in context.splitlines():
                # print(line)
                regx = "u0 (.*?)/"
                result = re.findall(regx, line)
                com.close()
                break
            apk.append(result[0])

            print("未输入包名，默认包名:", apk)
    else:
        print("输入的包名：", apk)

    # 限制执行步数只能输入int类型
    times = input("输入要执行时常时间（默认9000分钟）：")
    if not re.findall('^[0-9]+$', times):
        # 输入的数值不符合规则，给一个默认值9000
        times = 9000
        print("默认执行时长（关闭窗口即可终止monkey）：", times)
    else:
        print("输入执行时长（关闭窗口即可终止monkey）：", times)
    # 对多个设备执行monkey命令
    j = 0
    for i in devices_list:
        maxin = 'start adb -s ' + i + ' shell "CLASSPATH=/sdcard/monkey.jar:/sdcard/framework.jar exec app_process /system/bin tv.panda.test.monkey.Monkey -p ' + apk[j] + '  --uiautomatormix --running-minutes {0} -v -v'.format(
            times)
        with open(os_path + f'\\{i}start.bat', 'w+') as f:
            f.write(maxin)
        os.system(os_path + f'\\{i}start.bat')
        os.popen('del ' + os_path + f'\\{i}start.bat')
        if len(apk) > 1:
            j = j + 1

def download_install():
    image_name = 'qr_image.png'
    url = input("请输入URL：")
    start = time.time()
    response = urllib.request.urlopen(url)
    print("正在下载...")
    data = response.read()
    with open(fr'{os_path}\APK\app.apk', 'wb') as file:
        file.write(data)
    end = time.time() - start
    print("下载完毕耗时：{:.0f}m {:.0f}s".format(end // 60, end % 60))
    file_name = 'app.apk'
    if os.path.exists(fr'APK\{file_name}'):
        print("安装包准备就绪正在安装...")
        cmd = r'adb install -r {0}\APK\{1}'.format(os_path, file_name)
        install = os.popen(cmd)
        install_txt = install.read()
        for line in install_txt.splitlines():
            if line == "Success":
                print("安装成功：", line)
            else:
                print("安装失败：", line)
                print(r"可扫码安装：{}\{}".format(os_path, image_name))
                # 安装失败将url转换成二维码图片
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=1
                )
                qr.add_data(url)
                qr.make(fit=True)
                img = qr.make_image()
                img.save(r'{}\images\{}'.format(os_path, image_name))
                if os.path.exists(fr'images\{image_name}'):
                    show_image = Image.open(fr'images\{image_name}')
                    show_image.show()
                else:
                    print("图片不存在！")
if __name__ == '__main__':
    # 判断文件夹是否存在不存在则创建
    if os.path.exists('images'):
        pass
    else:
        os.mkdir('images')
    if os.path.exists('log'):
        pass
    else:
        os.mkdir('log')
    if os.path.exists('APK'):
        pass
    else:
        os.mkdir('APK')

    while True:
        devices_list = get_deviceid()
        if devices_list:  # 判断设备列表是否为空,空则不显示菜单
            print("-" * 100, "\n已连接设备:", devices_list, lists, "-" * 100)
            try:
                a = int(input("请输入编号:"))
                if a in list:
                    if a == 1:
                        # 获取文件路径
                        push_path = input("拖动文件:")
                        adb_push(push_path)
                    elif a == 2:
                        adb_pm()
                        # 清除缓存
                    elif a == 3:
                        path = str(input("把安装包拖到这里:"))
                        while path == '':
                            path = input("\n未获取到安装包路径:")
                        adb_install(path)
                    #     安装应用_支持多台
                    elif a == 4:
                        adb_com()
                    #     查看包名
                    elif a == 5:
                        adb_screen()
                    #     截图
                    elif a == 6:
                        Package = str(input("输入包名（默认前台APP）:"))
                        adb_uninstall(Package)
                    #     卸载当前app
                    elif a == 7:
                        adb_monkey()
                    #     Monkey*
                    elif a == 8:
                        adb_monkeys()
                    #     Monkey_诸葛
                    elif a == 9:
                        adb_reboot()
                    #     重启
                    elif a == 10:
                        adb_cache()
                    #     清缓存_诸葛
                    elif a == 11:
                        adb_logcat()
                    elif a == 12:
                        adb_maxim(os_path)
                    elif a == 13:
                        download_install()
                    elif a == 0:
                        print("Ended！")
                        break
                else:
                    print("编号错误,请重新输入!!!")
            except ValueError as e:
                print(e)
                pass
            except IndexError as e:
                print(e)
                pass
            except UnboundLocalError as e:
                print(e)
                pass
        else:
            input("未检测到设备！请确保手机已开启调试，按Enter重新检查设备。")
