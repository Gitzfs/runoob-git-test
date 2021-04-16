# 导入封装好的请求类
import allure
from configfile.Assert import Assert_class
from configfile.Request_class import RequestsClass
import json
from configfile import load_yaml_data

@allure.description("信息流接口")
@allure.testcase('http://bug.com/user-login-Lw==.html', name='测试接口')
def test_information():
    # 读取yaml内的数据
    yaml_data = load_yaml_data.load_data('./yaml_data/yaml_request_data.yaml')
    # 调用RequestsClass类的post_req方法请求接口
    response = RequestsClass().post_req(URL=yaml_data['test_information']['URL'],
                                        data=json.dumps(yaml_data['test_information']['data']),
                                        headers=yaml_data['test_information']['headers'])
    response.status_code
    # print(response.json())
    response_txt = response.json()
    result = json.dumps(response_txt, indent=3, sort_keys=True, ensure_ascii=False)
    print("请求状态：{}\n响应数据：{}\n校验字段：{}".format(response.status_code, result, response_txt['msg']))
    # assert response_txt['msg'] == data['test_information']['exp_code']['msg'], '失败'
    # print(response_txt['msg'], yaml_data['test_information']['exp_code']['msg'])
    Assert_class().assert_msg(msg=response_txt['msg'], exp_msg=yaml_data['test_information']['exp_code']['msg'])
    Assert_class().assert_code(code=response_txt['code'], exp_code=yaml_data['test_information']['exp_code']['code'])
    Assert_class().assert_code(req_code=response.status_code, exp_recode=yaml_data['test_information']['exp_code']['req_code'])
