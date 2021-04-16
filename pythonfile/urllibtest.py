# -*- coding:utf-8 -*-

import os
import time
import urllib.request
from urllib import error
import qrcode
from PIL import Image
os_path = os.getcwd()

while True:
    '''限制输入，空：重新入，0取消下载跳出循环'''
    url = input("请输入URL：")
    while url == '':
        url = input("请重新输入URL(0取消下载)：")
    if url == '0':
        cancel = False
        break
    else:
        cancel = True
    try:
        '''urllib.request.urlopen()函数用于实现对目标url的访问。'''
        start = time.time()
        response = urllib.request.urlopen(url)
        print("正在下载...")
        data = response.read()
        # 重命名以.apk格式存储到本地，并检测是否存在
        with open('app.apk', 'wb') as file:
            file.write(data)
        end = time.time() - start
        print("下载完毕耗时：{:.0f}m {:.0f}s".format(end // 60, end % 60))
        cancel = True
        break
    except error.HTTPError as e:
        print("请求失败：", e.code)
    except error.URLError as e:
        print("请求失败：", e.reason)
    except UnicodeEncodeError:
        print("格式错误！")
    except ValueError:
        print("格式错误！")
if cancel is True:
    filename = 'app.apk'
    img_filename = 'my_blog.png'

    if os.path.exists(filename):
        cmd = r'adb install -r {0}\{1}'.format(os_path, filename)
        print("安装包准备就绪,正在安装...")
        install = os.popen(cmd)
        context = install.read()
        for line in context.splitlines():
            # print(line)
            results = line
            if results == "Success":
                print("安装成功：", results)
            else:
                print("安装失败：", results)
                print(r"扫码安装：{}\{}".format(os_path, img_filename))
                url = url
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=1
                )  # 设置二维码的大小
                qr.add_data(url)
                qr.make(fit=True)
                img = qr.make_image()
                img.save(r'{}\Images\{}'.format(os_path, img_filename))

                # os.remove(r'{}\{}'.format(os_path, img_filename))

                if os.path.exists(img_filename):
                    im = Image.open(img_filename)
                    im.show()
                else:
                    print("图片不存在在！")
    else:
        print("安装失败，未检测到安装包!")
# 安装完成删除安装包
os.remove(r'{}\{}'.format(os_path, filename))


