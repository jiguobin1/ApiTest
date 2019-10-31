# -*- coding: utf-8 -*- 
# @Time : 2019/10/22 9:44 
# @Author : Ji
# @File : test01case.py
import json
import unittest
import HTMLTestRunner
from common.configHttp import RunMain
from testFile import geturlParams
from testFile.readExcel import readExcel
from testFile.getpathInfo import get_Path
from BeautifulReport import BeautifulReport
url = geturlParams.geturlParams().get_Url()# 调用我们的geturlParams获取我们拼接的URL


class testUserLogin(unittest.TestCase):
    def setUp(self):
        print ("测试用例： {0}...".format(self._testMethodName))
        pass

    def test01case(self):
        u'''用例1：登录正常系'''
        data=readExcel().get_excel_info('login',2)  #获取用例数据值，转换成为map类型
        self.info=RunMain().run_main('post',url, data)
        ss = json.loads(self.info)# 将响应转换为字典格式
        self.assertEqual(ss['code'],200)
        self.assertEqual(ss['message'],'登录成功',)


    def test02case(self):
        u'''用例2：错误密码登录'''
        data=readExcel().get_excel_info('login',3)
        self.info=RunMain().run_main('post',url, data)
        ss = json.loads(self.info)# 将响应转换为字典格式
        self.assertEqual(ss['code'],200)
        self.assertEqual(ss['message'],'登录成功')

    def tearDown(self):
        print ('响应结果:',self.info)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(testUserLogin('test01case'))
    suite.addTest(testUserLogin('test02case'))
    test_suite = unittest.defaultTestLoader.discover(get_Path(), pattern='test*.py')
    result = BeautifulReport(suite)
    result.report(filename='login测试报告', description='测试deafult报告', log_path='report')
    suite=unittest.main()



