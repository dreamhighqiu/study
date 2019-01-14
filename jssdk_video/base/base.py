# -*- coding: utf-8 -*-
'''
Created on ：2018/7/25:12:02

@author: yunxia.qiu
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time,os
class base_func():
    def __init__(self,driver):
        self.driver=driver

    def launch_chrome(self):
        mobile_emulation = {"deviceName": "iPhone 6"}
        options = Options()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        options.add_argument("disable-infobars")
        self.driver = webdriver.Chrome(chrome_options=options)
        return self.driver

    def close_chrome(self):
        self.driver.quit()

    def get_screen_shot(self,title):
        cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        str_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(int(time.time())))

        real_path_no = os.path.join(cur_path, "jpg/%s-%s.png" % (str_time, title))
        self.driver.get_screenshot_as_file(real_path_no)

    def get_screen_shot(self,title,time_val=1):
        time.sleep(time_val)
        cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        str_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(int(time.time())))

        real_path_no = os.path.join(cur_path, "jpg/%s-%s.png" % (str_time, title))
        self.driver.get_screenshot_as_file(real_path_no)

    def get_circle_screen_shot(self, title,waittime,count):

        for i in range(count):
            self.get_screen_shot(title,waittime)





