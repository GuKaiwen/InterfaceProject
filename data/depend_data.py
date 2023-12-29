from util.operation_excel import OperationExcel
from data.get_data import GetData
from basic.run_method import RunMethod
from jsonpath_rw import jsonpath, parse
import json

class DependData:

    def __init__(self, case_id=None):
        self.opera_excel = OperationExcel()
        self.data = GetData()
        self.run_method = RunMethod()
        self.case_id = case_id

    def get_depend_row_data(self):
        depend_row_data = self.opera_excel.get_depend_data(self.case_id)
        return depend_row_data

    def run_depend_data(self):
        depend_row_num = self.opera_excel.get_row_num(self.case_id)
        url = self.data.get_url(depend_row_num)
        data = self.data.get_request_data(depend_row_num)
        method = self.data.get_method(depend_row_num)
        res = self.run_method.run_main(method, url, data)
        return json.loads(res)

    def get_data_for_key(self, row):
        depend_key = self.data.get_depend_data(row)
        response_data = self.run_depend_data()
        json_exe = parse(depend_key)
        madle = json_exe.find(response_data)
        return [math.value for math in madle]



if __name__ == '__main__':
    depend_data = DependData('imooc-08')
    print(depend_data.get_depend_row_data())
    print(depend_data.run_depend_data())

