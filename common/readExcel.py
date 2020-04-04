import xlrd
import os
workspace = os.path.abspath(__file__)
commonPath = os.path.dirname(os.path.dirname(workspace))
datafilePath = commonPath+r'\testData\dataC.xls'
print(workspace)
print(datafilePath)

class readExcel(object):
    def __init__(self):
        self.workbook = xlrd.open_workbook(datafilePath)

    def read(self):
        # 获取sheet页
        sheet = self.workbook.sheet_by_name('urlSheet')
        # 获取行数
        nows = sheet.nrows
        # 获取所有行数据
        data = []
        for i in range(1, nows):
            row = sheet.row_values(i)
            data.append(row)
        return data

if __name__ == '__main__':
    re = readExcel()
    print(re.read())