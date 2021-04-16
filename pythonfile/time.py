import os
'''time¼ÆÊ±Æ÷'''
filename = r'/home/tim/workspace/test.txt'

if os.path.exists(filename):
    message = 'OK, the %s file exists.' % filename
else:
    message = "Sorry, I cannot find the %s file." % filename
print(message)
