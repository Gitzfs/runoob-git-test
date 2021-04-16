# -*- coding:utf-8 -*-
import os
import qrcode
from PIL import Image

'''qrcode生成二维码'''
url = input("请输入URL：")
qr = qrcode.QRCode(
	version=1,
	error_correction=qrcode.constants.ERROR_CORRECT_L,
	box_size=10,
	border=1
)# 设置二维码的大小
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image()
img.save("my_blog.png")
if os.path.exists("my_blog.png"):
	image_name = 'my_blog.png'
	im = Image.open('my_blog.png')
	im.show()
else:
	print("图片不存在在！")



