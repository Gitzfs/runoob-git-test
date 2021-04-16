# 导入封装好的请求类
import allure
import pytest

from configfile.Request_class import RequestsClass
import json
from configfile import load_yaml_data

@allure.description("信息流接口")
@allure.testcase('http://bug.com/user-login-Lw==.html', name='测试接口')
# @pytest.mark.parametrize()
def test_information():
    # 读取yaml内的数据
    data = load_yaml_data.load_data('./yaml_data/yaml_request_data.yaml')
    # 调用RequestsClass类的post_req方法请求接口
    response = RequestsClass().post_req(URL=data['test_information']['URL'],
                                        data=json.dumps(data['test_information']['data']),
                                        headers=data['test_information']['headers'])
    # print(response.json())
    # print(response.status_code)
    response_txt = response.json()
    result = json.dumps(response_txt, indent=3, sort_keys=True, ensure_ascii=False)
    print("请求状态：{}\n响应数据：{}\n校验字段：{}".format(response.status_code, result, response_txt['msg']))
    assert response_txt['msg'] == data['test_information']['exp_code']['msg'], '失败'
