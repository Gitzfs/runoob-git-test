import yaml
import os

import yaml


class Yaml_Data:
    # 读取yaml数据

    def read_data_from_file(self=None):

        # 获取当前目录
        rootPath = os.path.dirname(os.path.abspath('.'))
        print(rootPath)
        """
        读取yaml文件的内容
        :param file_name
        """
        f = open(rootPath + '\\pytest_allure_test\\yaml_data' + '\\yaml_request_data.yaml', encoding='utf-8')
        res_json = yaml.load(f, Loader=yaml.FullLoader)  # 添加loader参数是为了去掉load warning
        return res_json
#         p = read_data_from_file()
#         print(p['test_information'])
#
# yaml_data=Yaml_Data
# print(yaml_data.read_data_from_file()['test_information'])



