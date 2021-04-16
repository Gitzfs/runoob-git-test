import yaml

# yaml格式内容的数据读取
def load_data(path):
    file = open(path, 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    print(type(data))
    return data

# print(load_data('../yaml_data/yaml_request_data.yaml'))