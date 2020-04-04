import xlrd,os
from xlutils.copy import copy
workspace = os.path.abspath(__file__)
commonPath = os.path.dirname(os.path.dirname(workspace))
datafilePath = commonPath+r'\testData\dataC.xls'

class writeExcel(object):
    def __init__(self):
        self.readbook = xlrd.open_workbook(datafilePath)
        self.writebook = copy(self.readbook)
        self.wsheet = self.writebook.get_sheet(0)

    def write(self,real,status,x=0,y=0):
        self.wsheet.write(x,y,real)
        self.wsheet.write(x,y+1,status)
        self.writebook.save(datafilePath)

if __name__ == '__main__':
    we = writeExcel()
    we.write("XC")