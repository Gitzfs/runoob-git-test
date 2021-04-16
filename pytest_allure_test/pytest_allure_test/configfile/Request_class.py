import requests
import json
class RequestsClass:
    '''
    POST和GET请求类：RequestsClass
    '''
    def post_req(self,URL,data,headers,**kwargs):
        '''
        POST请求
        :param URL:
        :param data:
        :param headers:
        :param kwargs:
        :return:
        '''
        response = requests.post(url=URL,data=data,headers=headers,**kwargs)
        return response
    def get_req(self,URL, data, **kwargs):
        '''
        GET请求
        :param URL:
        :param data:
        :param kwargs:
        :return:
        '''
        response = requests.get(url=URL,params=data,**kwargs)
        return response


