import HTMLTestRunner
import os
import unittest


base_dir = os.path.dirname(os.path.abspath('__file__'))
case_dir = base_dir + '\\' + 'testCase'
result_html = base_dir + '\\' + 'report' + '\\' + 'result.html'

def create_suite():
    discover = unittest.defaultTestLoader.discover(
        start_dir=case_dir,
        pattern='test*.py',
        top_level_dir=None
    )
    return discover

if __name__ == '__main__':
    suite = create_suite()
    print(suite)
    with open(result_html,'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title='自动化接口测试报告',
            description='详细报告'
        )
        runner.run(suite)
