"""
功能描述：

解析：
 1、获取url地址、请求数据、请求方式、请求预期结果数据
 2、判断是get请求还是post请求
 3、发送请求
 4、得到请求后的结果
 5、判断得到的时间结果与预期结果进行对比
 6、给出最终结论
"""
import unittest
from ddt import ddt,data,unpack
from common.readExcel import readExcel
from common.writeExcel import writeExcel
from common.confighttp import configHttp

@ddt
class MyTestCase(unittest.TestCase):
    # 调用readExcel模块
    re = readExcel()
    test_data = re.read()
    # 2-根据接口测试数据，进行请求
    # id,url,desc,requestMethod,param,expect,real,status=test_data[0]
    # print(22222)
    @data(*test_data)
    @unpack
    def test_request(self,id,url,desc,method,param,expect,real,status):
        # print(id, url, desc, method, param, expect, real, status)
        print('-  -  ' * 20)
        conhttp = configHttp()
        status_code,error_code = conhttp.run(id,url,desc,method,param)
        print(id,status_code,error_code)
        wre = writeExcel()
        if str(status_code) == '200':
            if str(error_code) == expect:
                status = 'Successed'
                wre.write(str(error_code),status, int(id), 6)
                return True
            else:
                status = 'Failed'
                wre.write(str(error_code), status, int(id), 6)
                return False
        else:
            status = 'Failed'
            wre.write(str(error_code), status, int(id), 6)
            return False


if __name__ == '__main__':
    unittest.main()

