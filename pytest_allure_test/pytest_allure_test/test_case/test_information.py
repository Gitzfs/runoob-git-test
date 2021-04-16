# 导入封装好的请求类
import allure
import pytest
import yaml
# from requests_demo1.request_class import RequestsClass

import allure
from configfile.Request_class import RequestsClass
import json
from config.read_yaml_data import Yaml_Data

ym_dt = Yaml_Data
ym_dt.read_data_from_file()

@allure.description("信息流接口")
@allure.link('https://docs.pytest.org/en/latest',name='pytest帮助文档')
@allure.issue('http://baidu.com', name='点击我跳转百度')
@allure.testcase('http://bug.com/user-login-Lw==.html', name='点击我跳转禅道')
def test_information():
    # 调用RequestsClass类的post_req方法请求接口
    response = RequestsClass().post_req(URL=ym_dt.read_data_from_file()['test_information']['URL'],
                                        data=json.dumps(ym_dt.read_data_from_file()['test_information']['data']),
                                        headers=ym_dt.read_data_from_file()['test_information']['headers'])
    # print(response.json())
    # print(response.status_code)
    response_txt = response.json()
    result = json.dumps(response_txt, indent=3, sort_keys=True, ensure_ascii=False)
    print("请求状态：{}\n响应数据：{}\n校验字段：{}".format(response.status_code, result, response_txt['msg']))
    assert response_txt['msg'] == ym_dt.read_data_from_file()['test_information']['exp_code']['msg'], '失败'


# test_information(URL=URL, headers=Headers, data=DATA)