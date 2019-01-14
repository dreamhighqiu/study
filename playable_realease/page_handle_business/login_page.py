# -*- coding: UTF-8 -*-
'''
-*- coding: utf-8 -*-
@Author  : yunxia.qiu
@Time    : 2018/8/20 14:45
@Software: PyCharm
@File    : login_page.py.py
'''
# import sys
# sys.path.append("E:\\jssdk\\dsp-playable-jssdk")
# print(sys.path)
from selenium import webdriver
from playable_realease.base.base import base_func
from playable_realease.config.ParseConfigurationFile import ParseConfigfile
import os,time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
class Login_Page(base_func):
    def __init__(self,driver):
        super(Login_Page,self).__init__(driver)

        # self.bf =base_func(self.driver)



    def get_address_loc(self,address):
        self.input("login_loc","address",address)



    def get_password_loc(self,password):
        self.input("login_loc","password",password)

    def click_login(self):
        self.click("login_loc","login_ele")

    def release(self):
        self.click("login_loc","release")
        # self.bf.locs("login_loc","update")[1].click()

    def get_shop_loc(self, text):
        self.input("release_info", "shop_address", text)
    def get_launage_loc(self):
        time.sleep(3)
        self.click("release_info", "launage")

        loc_01=self.loc("release_info", "launage_choice")
        time.sleep(3)
        ActionChains(self.driver).click(loc_01).perform()
    def get_offer_type_loc(self):
        self.click("release_info", "offer_type")
        type_loc=self.loc("release_info", "offer_type_choice")
        ActionChains(self.driver).click(type_loc).perform()

    def get_developer_loc(self):
        self.click("release_info", "developer")
        self.click("release_info", "developer_choice")

    def get_designer_loc(self):
        self.click("release_info", "designer")
        self.click("release_info", "designer_choice")
    def get_upload_loc(self):
        self.click("release_info","upload")
        time.sleep(3)
        os.system(r'E:\jssdk\dsp-playable-jssdk\playable_realease\exe\autoit_script.exe')
        ele =self.loc("release_info","update_success")
        time.sleep(15)
        if EC.visibility_of(ele):
            self.get_submit_loc()
        else:
            time.sleep(10)
            self.get_submit_loc()

    def get_submit_loc(self):
        self.click("release_info","submit_test")
    def update_submit(self):
        self.click("detail_info","update_sure")

    def run_login(self,address,password):
        self.get_address_loc(address)
        self.get_password_loc(password)
        self.click_login()
        self.driver.implicitly_wait(10)

    def run_release(self,value):
        self.release()
        self.get_shop_loc(value)
        self.get_launage_loc()
        self.get_offer_type_loc()
        self.get_developer_loc()
        self.get_designer_loc()
        self.get_upload_loc()
        # self.get_submit_loc()
        # self.driver.close()

    def get_window(self):
        # cur_handle=self.driver.current_window_handle()
        # print(cur_handle)
        print(self.driver.window_handles)

    def get_release_url(self):
        ele=self.loc("detail_info","preview")
        url=ele.get_attribute("href")
        dest_url=url.split("?")[0]
        print(dest_url)
    def preview_url(self):
        time.sleep(2)
        eles = self.locs("detail_info", "preview")
        # for i in range(len(eles)):
        for i in range(3):
            eles[i].click()
            switch_handle_all = self.driver.window_handles
            switch_handle=switch_handle_all[-1]
            self.driver.switch_to_window(switch_handle)
            url= self.driver.current_url
            dest_url = url.split("?")[0]
            print(dest_url)
            title = dest_url.split("/")[-1]
            self.get_screen_shot(title,10)
            self.driver.close()
            self.driver.switch_to_window(switch_handle_all[0])

        # eles = self.bf.locs("detail_info", "preview")[2].click()

    def switch_next_page(self):
        time.sleep(3)
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
        ele=self.loc("detail_info","next_page")
        if ele:
            ele.click()
            self.preview_url()


    def update_zip(self):
        time.sleep(3)
        self.click("detail_info","update")
        self.click("release_info","upload")
        time.sleep(3)
        os.system(r'E:\jssdk\dsp-playable-jssdk\playable_realease\exe\autoit_script.exe')
        time.sleep(15)
        self.input("detail_info","update_content",r"update content")
        self.update_submit()

    def run_main_release_zip(self,address,password,value):
        self.run_login(address,password)
        self.run_release(value)
        self.get_release_url()
    def run_main_update_zip(self,address,password):
        self.run_login(address, password)
        self.update_zip()
        self.get_release_url()

    def success_confire(self):
        ele=self.loc("success_confire","release").text
        return ele
if __name__ == "__main__":
    options = Options()
    # options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.add_argument("disable-infobars")
    # options.add_argument("headless")
    driver = webdriver.Chrome(chrome_options=options)
    url="http://playable-portal.mintegral.com/#/my/qa-list"
    driver.get(url)
    ll=Login_Page(driver)
    username = "yunxia.qiu@mintegral.com"
    password = "123456"
    address = 'https://itunes.apple.com/cn/app/war-robots/id806077016?mt=8'
    #更新zip包
    # ll.run_main_update_zip(username,password)
    #发布zip包
    # ll.run_main_release_zip(username,password,address)

    #获取预览内容以及地址
    ll.run_login(username,password)
    ll.preview_url()

    ll.switch_next_page()









