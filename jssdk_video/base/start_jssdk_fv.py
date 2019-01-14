# -*- coding: utf-8 -*-
'''
Created on ：2018/7/24:14:05

@author: yunxia.qiu
'''
# coding:utf-8
import os
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver import ActionChains
from jssdk_video.util.logger import Logger
import re
from jssdk_video.base.base import base_func
from selenium.webdriver.common.keys import Keys
logger = Logger(logger="jssdk_fv").getlog()

class jssdk_fv():
    def __init__(self):
        mobile_emulation = {"deviceName": "iPhone 8"}
        options = Options()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        options.add_argument("disable-infobars")
        options.add_argument("headless")
        self.driver = webdriver.Chrome(chrome_options=options)
        self.bf = base_func(self.driver)



    def get_loc(self,url,waittime,count,click_type=1):
        self.driver.implicitly_wait(3)
        self.driver.get(url)
        self.driver.implicitly_wait(5)
        # self.driver.execute_script("window.alert('这是一个测试Alert弹窗');")
        # time.sleep(2)
        # self.driver.switch_to_alert().accept()

        # try:
        #     lert = self.driver.switch_to_alert()
        #     result = lert.text
        #     # 模拟键盘Enter 键
        #     self.driver.implicitly_wait(3)
        #     ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        # except NoAlertPresentException as msg:
        #     print(msg)
        try:
            str_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(int(time.time())))
            self.driver.implicitly_wait(3)
            click_ele = self.driver.find_element_by_id("reward")
            print(click_ele)
            time.sleep(10)
            click_ele.click()
            frame = self.driver.find_element_by_xpath("//div/iframe")
            self.driver.switch_to_frame(frame)
            self.driver.implicitly_wait(3)
            mvvideoplayer = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "mvvideoplayer")))
            if mvvideoplayer:
                element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_class_name("title"))

                # element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "title")))
                title = element.text
                logger.info(u"----%soffer广告信息为--%r--" % (title, str_time))
                print(u"offer标题为:%s" % title)
                logger.info(u"offer标题为:%s" % title)
                icon = self.driver.find_element_by_xpath("//*[@id='cta']/div/div[1]/img").get_attribute("src")
                print(u"offer的icon为：%s" % icon)
                logger.info(u"offer的icon为：%s" % icon)
                video = self.driver.find_element_by_id("mvvideoplayer").get_attribute("src")
                print(u"offer的视频内容:%s" % video)
                logger.info(u"offer的视频内容:%s" % video)
                # notice_url = self.driver.find_element_by_id("cta").get_attribute("notice")
                # print(u"notice_url为：%s" % notice_url)
                # logger.info(u"notice_url为：%s" % notice_url)
                # click_url = self.driver.find_element_by_id("cta").get_attribute("click")
                # print(u"click_url为：%s" % click_url)
                # logger.info(u"click_url为：%s" % click_url)
                href_url = self.driver.find_element_by_id("cta").get_attribute("href")
                print(u"href_url为：%s" % href_url)
                logger.info(u"href_url为：%s" % href_url)
                agentclick_url = self.driver.find_element_by_id("cta").get_attribute(
                    "agentclick")
                print(u"agentclick_url为：%s" % agentclick_url)
                logger.info(u"agentclick_url为：%s" % agentclick_url)
                poster_url = self.driver.find_element_by_id("mvvideoplayer").get_attribute(
                    "poster")
                print(u"poster_url为：%s" % poster_url)
                logger.info(u"poster_url为：%s" % poster_url)
                self.bf.get_screen_shot(title)
                if click_type==1:
                    self.bf.get_circle_screen_shot(title,3,6)
                    download = self.driver.find_element_by_id("ctabtn")
                    download.click()
                    self.driver.implicitly_wait(3)

                    all_windows = self.driver.window_handles
                    if len(all_windows) == 2:
                        print(u"%s:点击跳转成功" % title)
                    else:
                        print(u"%s:点击跳转不成功" % title)
                    print(self.driver.current_url)
                else:
                    self.bf.get_circle_screen_shot(title,waittime,count)

                    self.endcard_url()
                self.driver.quit()
            else:
                print(u"无offer")
                self.driver.quit()


        except Exception as msg:
            print(u"异常信息---%s" % msg)
            print(u"无offer")

            self.driver.quit()

    def endcard_url(self):
        # print(111)
        # # self.driver.current_window_handle
        # # page = self.driver.find_element_by_xpath("//*[@id='endport']/div[2]/div[1]")
        # page = WebDriverWait(self.driver,10).until(lambda x:x.find_element_by_xpath("//*[@id='endport']/div[2]/div[1]"))
        #
        # print(222)
        # print(page)
        # style = page.get_attribute("style")
        # # background - image: url("http://cdn-adn.rayjump.com/cdn-adn/v2/offersync/18/05/28/15/08/5b0baae6db3a8.jpg");
        # page_url = re.findall(r"([\s|\S]*)",style)
        # print(page_url)
        # icon = self.driver.find_element_by_xpath('//*[@id="endport"]/div[2]/div[2]/div[1]/img').get_attribute("src")
        # print(icon)
        # title = self.driver.find_element_by_xpath('//*[@id="endport"]/div[2]/div[2]/h3').text
        # print(title)
        # install = self.driver.find_element_by_xpath('//*[@id="endport"]/div[2]/div[3]/div/a').click()
        # self.bf.get_screen_shot(title)
        print(111)
        self.driver.refresh()
        page = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//*[@id='endport']/div[1]/div[2]/img"))
        page_url = page.get_attribute("src")
        print(222)

        # print(222)
        # print(page)
        # style = page.get_attribute("style")
        # # background - image: url("http://cdn-adn.rayjump.com/cdn-adn/v2/offersync/18/05/28/15/08/5b0baae6db3a8.jpg");
        # page_url = re.findall(r"([\s|\S]*)", style)
        print(page_url)
        icon = self.driver.find_element_by_xpath('//*[@id="endport"]/div[1]/div[3]/div/div[1]/div[1]/img').get_attribute("src")
        print(icon)
        title = self.driver.find_element_by_xpath('//*[@id="endport"]/div[1]/div[3]/div/div[1]/div[2]/h3').text
        print(title)
        install = self.driver.find_element_by_xpath('//*[@id="endport"]/div[1]/div[3]/div/a').click()
        self.bf.get_screen_shot(title)







if __name__ == "__main__":
    # url = "https://pingan.i99pay.com/Public/bv.html"
    # jd = jssdk_bv()
    # jd.get_loc(url)


    count=1
    for i in range(count):
        # url = "https://pingan.i99pay.com/Public/fv.html"
        url_fv = "http://interactive.mintegral.com/qa_task/t253/v4/jssdk_830137/h/fv.html"
        jd = jssdk_fv()
        jd.get_loc(url_fv,3,4,1)

















