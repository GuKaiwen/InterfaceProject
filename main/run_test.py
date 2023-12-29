from basic.run_method import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from data.depend_data import DependData
from util.operation_header import OperationHeader
from util.operation_json import OperationJson


class RunTest:

    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.depend_data = DependData()

    def go_on_run(self):
        rows = self.data.get_row_numbers()
        for i in range(1, rows):
            url = self.data.get_url(i)
            is_run = self.data.get_is_run(i)
            method = self.data.get_method(i)
            data = self.data.get_request_data(i)
            expect = self.data.get_expect(i)
            denpend_case = self.data.get_depend_case(i)
            header = self.data.get_is_header(i)
            if is_run == 'yes':
                if denpend_case != "":
                    #获取依赖请求数据
                    denpend_data = self.depend_data.get_data_for_key(i)
                    #获取依赖字段
                    denpend_field = self.data.get_depend_field(i)
                    #修改请求数据依赖字段值
                    data[denpend_field] = denpend_data

                if header == 'write':
                    res = self.run_method.run_main(method, url, data)
                    opera_header = OperationHeader(res)
                    opera_header.write_cookie()
                elif header == 'yes':
                    opera_json = OperationJson('../dataconfig/cookie.json')
                    cookie = opera_json.get_data('apsid')
                    cookie = {
                        'apsid': cookie
                    }
                    res = self.run_method.run_main(method, url, data, header=cookie)
                else:
                    res = self.run_method.run_main(method, url, data)
                # res = self.run_method.run_main(method, url, data)
                if self.com_util.is_contain(expect, res):
                    self.data.write_data(i, 'pass')
                else:
                    self.data.write_data(i, res)
                # print(res)

if __name__ == '__main__':
    run_test = RunTest()
    run_test.go_on_run()

