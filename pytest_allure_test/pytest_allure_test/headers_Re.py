import json

# 将信息头赋给变量headers
headers = """
Content-Type: application/json;charset=utf-8
env: ErVbrAcgeqx4rnvigsxU9KcF5yt4RJfsXOoBl9Mxqgp9O/vwd24KZzk2BpSCVpXVILvZSsWRaIjlrhB8DRT5Hw==
group: MX+SWMgU4DqH+euS75OOpxN3ROzeU7ap6VuiLx9ssWKmqOka9/DbmrXmtaJUW5T6VPgZRprkXDBgiBLsKZmcEA==
platform-id: mtJrYxVbj/i0pSdxPY5TUO3hqNtcGhan8P/4wWLCRrnw7XcmXeoww6ir/tK4DSrA/CXNzoIXtAUJrPCNl7RGbA==
source: 3
os_system: 1
osSystem: 1
app-id: 
token: 
UserId: -1
sign: 
timestamp: 1618300369996
uuid: 20adc17af5280d89
version: 4.14
ua: luckCalendar%2F4.14%2FDalvik%2F2.1.0+%28Linux%3B+U%3B+Android+10%3B+PBET00+Build%2FQKQ1.190918.001%29
appSign: 630A93500595AD9DB58C382B820E0D79
channel: jrl_oppo
bid: 34
userActive: 1618300370086
versionCode: 88
productName: jirili
bizCode: zhugewannianli
oaid: 02D0B7146CE348F7BA0B0F8FD15CDD24bc3ff2f85c294d6979c1d5e96676aa24
loginUserId: 
loginToken: 
Host: calapi.51jirili.com
Connection: Keep-Alive
Accept-Encoding: gzip
User-Agent: okhttp/4.8.1

"""

# 去除参数头尾的空格并按换行符分割
headers = headers.strip().split('\n')
print(headers)
# 使用字典生成式将参数切片重组，并去掉空格，处理带协议头中的://
headers = {x.split(':')[0].strip(): ("".join(x.split(':')[1:])).strip().replace('//', "://") for x in headers}
print(type(headers))
# 使用json模块将字典转化成json格式打印出来
print(json.dumps(headers, indent=1))