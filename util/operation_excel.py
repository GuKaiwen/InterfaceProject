import xlrd
from xlutils.copy import copy

class OperationExcel:

    def __init__(self, filename=None, sheet_id=None):
        if filename:
            self.filename = filename
            self.sheet_id = sheet_id
        else:
            self.filename = '../dataconfig/testcases.xls'
            self.sheet_id = 0
        self.data = self.get_data()

    def get_data(self):
        data = xlrd.open_workbook(self.filename)
        table = data.sheets()[self.sheet_id]
        return table

    def get_row_numbers(self):
        return self.data.nrows

    def get_row_data(self):
        return self.data.row_value()

    def get_cell_data(self, row, col):
        return self.data.cell_value(row, col)

    def write_data(self, row, col, value):
        #对excel进行复制，不是table
        read_data = xlrd.open_workbook(self.filename)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.filename)

    #根据case_id获取行内容
    def get_depend_data(self, case_id):
        row_num = self.get_row_num(case_id)
        row_value = self.get_row_value(row_num)
        return row_value

    #根据case_id获取行号
    def get_row_num(self, case_id):
        num = 0
        col_values = self.get_col_values()
        for col_value in col_values:
            if case_id == col_value:
                return num
            num += 1
        return num

    #根据行号获取行内容
    def get_row_value(self, row):
        return self.data.row_values(row)

    #根据列获取列内容
    def get_col_values(self, col=None):
        if col != None:
            return self.data.col_values(col)
        else:
            return self.data.col_values(0)

if __name__ == '__main__':
    opera_excel = OperationExcel()
    print(opera_excel.get_row_numbers())
    print('get_row_num:'+str(opera_excel.get_row_num('imooc-08')))
    print(opera_excel.get_col_values())
    print(opera_excel.get_depend_data('imooc-08'))