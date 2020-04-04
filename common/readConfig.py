import configparser
import os
filepath = os.path.dirname(os.path.abspath(__file__))

class MyConf(object):
    def __init__(self,filename):
        self.filename = filename
        self.conf = configparser.ConfigParser()
        self.conf.read(self.filename,encoding='utf-8')
    def getValue(self,section,option):
        result = {}
        for item in self.conf.sections():
            itemdic = {}
            for opt in self.conf.options(item):
                value = self.conf.get(item,opt)
                itemdic[opt] = value
            result[item] = itemdic
        # print(result)
        if section in result.keys():
            if option in result[section].keys():
                return result[section][option]
            else:
                print("Option在配置文件中不存在，请检查是否正确...")
                return
        else:
            print("Section在配置文件中不存在，请检查填写是否正确...")
            return




if __name__ == '__main__':
    configFile = os.path.dirname(filepath)+'\config.ini'
    myconf = MyConf(configFile)
    print(myconf.getValue('EMAIL','mail_hos'))