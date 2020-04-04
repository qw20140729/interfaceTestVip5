import requests

class configHttp(object):

    def run(self,id,url,desc,method,param):
        # print(id,url,desc,method,param)
        if method == 'get' or method == 'GET':
            return self.get(url,param)
        if method == 'post' or method == 'POST':
            return self.post(url,param)
        if method == 'put' or method == 'PUT':
            return self.put(url,param)

    def get(self,url,param):
        result = requests.get(url=url,params=eval(param))
        status_code = result.status_code
        error_code = result.json()['errorCode']
        return status_code,error_code

    def post(self,url,param):
        print(url,param)
        result = requests.post(url=url, data=eval(param))
        status_code = result.status_code
        error_code = result.json()['errorCode']
        # print(status_code,error_code)
        return status_code, error_code

    def put(self,url,param):
        result = requests.put(url=url, data=param)
        status_code = result.status_code
        error_code = result.json()['errorCode']
        return status_code, error_code
