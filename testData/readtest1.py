import xlrd

# 打开文件
workbook = xlrd.open_workbook('dataC.xls')
# 获取sheet页
sheet = workbook.sheet_by_name('urlSheet')
# 获取行数
nows = sheet.nrows
# 获取所有行数据
data = []
for i in range(1,nows):
    row = sheet.row_values(i)
    data.append(row)
print(data)

