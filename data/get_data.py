from dataconfig import data_config
from util.operation_excel import OperationExcel
from util.operation_json import OperationJson

class GetData:

    def __init__(self):
        self.opera_excel = OperationExcel()

    def get_row_numbers(self):
        return self.opera_excel.get_row_numbers()

    def get_id(self, row):
        col = int(data_config.get_id())
        return self.opera_excel.get_cell_data(row, col)

    def get_mode(self, row):
        col = int(data_config.get_mode())
        return self.opera_excel.get_cell_data(row, col)

    def get_url(self, row):
        col = int(data_config.get_url())
        return self.opera_excel.get_cell_data(row, col)

    def get_is_run(self, row):
        col = int(data_config.get_is_run())
        return self.opera_excel.get_cell_data(row, col)

    def get_method(self, row):
        col = int(data_config.get_method())
        return self.opera_excel.get_cell_data(row, col)

    def get_is_header(self, row):
        col = int(data_config.get_is_header())
        return self.opera_excel.get_cell_data(row, col)

    def get_depend_case(self, row):
        col = int(data_config.get_depend_case())
        return self.opera_excel.get_cell_data(row, col)

    def get_depend_data(self, row):
        col = int(data_config.get_depend_data())
        return self.opera_excel.get_cell_data(row, col)

    def get_depend_field(self, row):
        col = int(data_config.get_depend_field())
        return self.opera_excel.get_cell_data(row, col)

    def get_request_data(self, row):
        col = int(data_config.get_request_data())
        return self.opera_excel.get_cell_data(row, col)

    def get_data_for_json(self, row):
        opera_json = OperationJson()
        return opera_json.get_data(self.get_request_data(row))

    def get_expect(self, row):
        col = int(data_config.get_expect())
        return self.opera_excel.get_cell_data(row, col)

    def get_result(self, row):
        col = int(data_config.get_result())
        return self.opera_excel.get_cell_data(row, col)

    def write_data(self, row, value):
        col = int(data_config.get_result())
        self.opera_excel.write_data(row, col, value)

if __name__ == '__main__':
    get_data = GetData()
    print(get_data.get_row_numbers())