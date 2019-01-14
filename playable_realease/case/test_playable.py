#coding=utf-8
'''
-*- coding: utf-8 -*-
@Author  : yunxia.qiu
@Time    : 2018/8/27 12:51
@Software: PyCharm
@File    : 11_test_playable.py
'''
import unittest
import HTMLTestRunner_jpg
import os
from selenium import webdriver
from playable_realease.util.logger import Logger
from playable_realease.util.logger_new import Logger_new
from selenium.webdriver.chrome.options import Options
from playable_realease.page_handle_business.login_page import Login_Page
import time,sys
from playable_realease.base.base import base_func
from ddt import ddt,data,unpack
from datetime import datetime
import datetime
log=Logger("Test_Playable").logger
# log_new=Logger_new("Test_Playable").logger
@ddt
class Test_Playable(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setupclass")
        # # mobile_emulation = {"deviceName": "iPhone 8"}
        # options = Options()
        # # options.add_experimental_option("mobileEmulation", mobile_emulation)
        # options.add_argument("disable-infobars")
        # # options.add_argument("headless")
        # cls.driver = webdriver.Chrome(chrome_options=options)
        # cls.driver.get("http://playable-portal.mintegral.com/#/my/qa-list")
        # cls.driver.maximize_window()
        # self.driver=webdriver.Edge()
    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.close()
        else:
            pass



    def setUp(self):
        case_name = self._testMethodName
        log.info(u"%s:用例开始执行"%case_name)
        # mobile_emulation = {"deviceName": "iPhone 8"}
        options = Options()
        # options.add_experimental_option("mobileEmulation", mobile_emulation)
        options.add_argument("disable-infobars")
        options.add_argument("headless")
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get("http://playable-portal.mintegral.com/#/my/qa-list")
        self.driver.maximize_window()
        # self.bf = base_func(self.driver)
        self.lp = Login_Page(self.driver)

    def tearDown(self):
        time.sleep(2)
        self.case_name = self._testMethodName
        if sys.exc_info()[0]:
            # self.bf = base_func(self.driver)
            self.lp.get_screen_shot(self.case_name)
        log.info(u"\n\n%s:用例执行结束" %self.case_name)
        self.driver.close()

    @data([r"yunxia.qiu@mintegral.com","123456"],[r"yunxia.qiu@mobvista.com","yunxia.qiu"])
    @unpack
    # @unittest.skip
    def test_login_success(self,address,password):
        self.lp.run_login(address,password)
        text=self.lp.success_confire()
        self.assertEqual(text,u"发起提测")

    @data([r"yunxia.qiu@mintegral.com", "123456"])
    @unpack
    # @unittest.skip
    def test_get_release_url(self,address,password):
        self.lp.run_login(address,password)
        self.lp.get_release_url()


    # @unittest.skip
    @data([r"yunxia.qiu@mintegral.com", "123456"])
    @unpack
    def test_get_preview_url(self, address, password):
        self.lp.run_login(address,password)

        self.lp.preview_url()
        self.lp.switch_next_page()


    @data((r"yunxia.qiu@mintegral.com", "123456","https://itunes.apple.com/cn/app/war-robots/id806077016?mt=8"))
    @unpack
    # @unittest.skip
    def test_run_main_release_zip(self,address,password,value):
        self.lp.run_main_release_zip(address,password,value)
        text = self.lp.success_confire()
        self.assertEqual(text, u"发起提测")

    @data((r"yunxia.qiu@mintegral.com", "123456"))
    @unpack
    # @unittest.skip
    def test_run_main_update_zip(self,address,password):
        self.lp.run_main_update_zip(address,password)
        text = self.lp.success_confire()
        self.assertEqual(text, u"发起提测")

if __name__ == "__main__":
    #方法1
    suite =unittest.TestSuite()
    suite.addTest(Test_Playable("test_login_success"))
    suite.addTest(Test_Playable("test_get_release_url"))
    suite.addTest(Test_Playable("test_get_preview_url"))
    suite.addTest(Test_Playable("test_run_main_release_zip"))
    suite.addTest(Test_Playable("test_run_main_update_zip"))



    #方法2：
    # base_path = os.path.dirname(os.path.dirname(__file__))
    # case_cur_path = os.path.join(base_path, "/case")
    # suite=unittest.defaultTestLoader.discover(case_cur_path,"test*.py")

    #方法3：
    # suite =unittest.TestLoader.loadTestsFromTestCase("Test_Playable")

    # run=unittest.TextTestRunner()
    # run.run(suite)

    base_path=os.path.dirname(os.path.dirname(__file__))
    cur_path=os.path.join(base_path,"/report")
    now=datetime.now().strftime("%Y-%m-%d-%H_%M_%S")
    report_path =cur_path+"/"+now+"_HtmlReport.html"
    print(report_path)
    file_path=file(report_path,"wb")
    runner=HTMLTestRunner_jpg.HTMLTestRunner(file_path,title="测试报告标题",description="测试报告描述")
    runner.run(suite)





