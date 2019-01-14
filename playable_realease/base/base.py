# -*- coding: utf-8 -*-
'''
Created on ：2018/7/25:12:02

@author: yunxia.qiu
'''
from playable_realease.config.ParseConfigurationFile import ParseConfigfile
from selenium import webdriver
import os,time
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from playable_realease.util.logger import Logger
import sys
import traceback
log=Logger("base_func").getlog()
class base_func(object):
    def __init__(self,driver):
        self.driver=driver
        self.pc = ParseConfigfile()


        # self.driver=self.launch_chrome()





    # def launch_chrome(self):
    #     # mobile_emulation = {"deviceName": "iPhone 8"}
    #     options = Options()
    #     # options.add_experimental_option("mobileEmulation", mobile_emulation)
    #     options.add_argument("disable-infobars")
    #     # options.add_argument("headless")
    #     self.driver = webdriver.Chrome(chrome_options=options)
    #     # self.driver=webdriver.Edge()
    #     return self.driver

    # def close_chrome(self):
    #     self.driver.quit()



    def get_screen_shot(self,title,time_val=1):
        time.sleep(time_val)
        cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        str_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(int(time.time())))

        real_path_no = os.path.join(cur_path, "jpg/%s-%s.png" % (str_time, title))
        self.driver.get_screenshot_as_file(real_path_no)


    def get_circle_screen_shot(self, title,waittime,count):

        for i in range(count):
            self.get_screen_shot(title,waittime)


    def loc(self,section,optionname,time=20):

        loc=self.pc.getOptionValue(section,optionname)
        loc_type,loc_value=loc.split("=>")[0],loc.split("=>")[1]
        loc_type=eval('By.%s'%loc_type)
        try:
            ele = WebDriverWait(self.driver, time).until(EC.visibility_of_element_located((loc_type, loc_value)))
            # ele = WebDriverWait(self.driver,time).until(EC.visibility_of_element_located((loc_type,loc_value)))
            # print(ele)
            log.info("******定位成功******：定位方式:%s,定位内容:%s" % (loc_type, loc_value))
            if ele:
                return ele

        except NoSuchElementException as msg:
            raise msg
        finally:
            if sys.exc_info()[0]:
                var = traceback.format_exc()
                log.info("xxxxxx定位失败xxxxxx：定位方式:%s,定位内容:%s\n定位失败原因:%s" % (loc_type, loc_value, var))
                return None
                # e_type, e_value, e_traceback = sys.exc_info()
                # log.info("type ==> %s"%(e_type.__name__))
                # log.info("value ==> %s" %(e_value.message))
                # log.info("traceback ==> file name: %s" %(e_traceback.tb_frame.f_code.co_filename))
                # log.info("traceback ==> line no: %s" %(e_traceback.tb_lineno))
                # log.info("traceback ==> function name: %s" %(e_traceback.tb_frame.f_code.co_name))





    def locs(self,section,optionname,time=20):

        loc=self.pc.getOptionValue(section,optionname)
        loc_type,loc_value=loc.split("=>")[0],loc.split("=>")[1]
        loc_type=eval('By.%s'%loc_type)
        # log.info("定位方式:---->%s,定位内容:--->%s" % (loc_type, loc_value))
        # print(loc_type,loc_value)

        try:
            ele = WebDriverWait(self.driver,time).until(lambda x:x.find_elements(loc_type,loc_value))
            # ele = WebDriverWait(self.driver,time).until(EC.visibility_of_element_located((loc_type,loc_value)))
            # print(ele)
            log.info("******定位成功******：定位方式:%s,定位内容:%s" % (loc_type, loc_value))
            if ele:
                return ele

        except NoSuchElementException as msg:
            raise msg
        finally:
            if sys.exc_info()[0]:
                var = traceback.format_exc()
                log.info("xxxxxx定位失败xxxxxx：定位方式:%s,定位内容:%s\n定位失败原因:%s" % (loc_type, loc_value, var))
                return None

    def click(self,section,optionname):
        self.loc(section,optionname).click()


    def input(self,section,optionname,text):
        self.loc(section, optionname).send_keys(text)









