

class Assert_class:
    """
    断言类
    """
    def request_code(self, req_code, exp_recode):
        """
        请求状态断言
        :param req_code: 请求状态码
        :param exp_recode: 预期状态码
        :return:
        """
        assert req_code == exp_recode, '失败'

    def assert_code(self, code, exp_code):
        """
        code断言
        :param code: 实际code
        :param exp_code: 预期code
        :return:
        """
        assert code == exp_code, '失败'


    def assert_msg(self, msg, exp_msg):
        """
        msg断言
        :param msg: 实际code
        :param exp_msg: 预期exp_msg
        :return:
        """
        assert msg == exp_msg, '失败'

