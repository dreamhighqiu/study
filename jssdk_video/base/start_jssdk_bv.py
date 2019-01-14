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
from jssdk_video.base.base import base_func
from jssdk_video.util.logger import Logger
logger = Logger(logger="jssdk_bv").getlog()

class jssdk_bv():
    def __init__(self):
        mobile_emulation = {"deviceName": "iPhone 8"}
        options = Options()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        options.add_argument("disable-infobars")
        options.add_argument("headless")
        self.driver = webdriver.Chrome(chrome_options=options)
        self.bf = base_func(self.driver)



    def get_loc(self,url,waittime,count_c):
        self.driver.get(url)
        result = EC.alert_is_present()(self.driver)
        if result:
            print(result.text)
            result.accept()
        else:
            print(u"alert未弹出")
            try:
                str_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(int(time.time())))
                self.driver.implicitly_wait(3)
                frame = self.driver.find_element_by_xpath("//div/iframe")
                self.driver.switch_to_frame(frame)
                self.driver.implicitly_wait(3)
                mvvideobannerplayer = self.driver.find_element_by_id("mvvideobannerplayer")
                if mvvideobannerplayer:
                    element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id("title"))

                    # element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "title")))
                    title = element.text
                    logger.info(u"----%soffer广告信息为--%r--" % (title,str_time))
                    print(u"offer标题为:%s" % title)
                    logger.info(u"offer标题为:%s" % title)
                    icon = self.driver.find_element_by_id("icon").get_attribute("src")
                    print(u"offer的icon为：%s" % icon)
                    logger.info(u"offer的icon为：%s" % icon)
                    video = self.driver.find_element_by_tag_name("video").get_attribute("src")
                    print(u"offer的视频内容:%s" % video)
                    logger.info(u"offer的视频内容:%s" % video)
                    notice_url = self.driver.find_element_by_xpath("//*[@id='info_warp']").get_attribute("notice")
                    print(u"notice_url为：%s" % notice_url)
                    logger.info(u"notice_url为：%s" % notice_url)
                    click_url = self.driver.find_element_by_xpath("//*[@id='info_warp']").get_attribute("click")
                    print(u"click_url为：%s" % click_url)
                    logger.info(u"click_url为：%s" % click_url)
                    href_url = self.driver.find_element_by_xpath("//*[@id='info_warp']").get_attribute("href")
                    print(u"href_url为：%s" % href_url)
                    logger.info(u"href_url为：%s" % href_url)
                    agentclick_url = self.driver.find_element_by_xpath("//*[@id='info_warp']").get_attribute(
                        "agentclick")
                    print(u"agentclick_url为：%s" % agentclick_url)
                    logger.info(u"agentclick_url为：%s" % agentclick_url)
                    poster_url = self.driver.find_element_by_id("mvvideobannerplayer").get_attribute(
                        "poster")
                    print(u"poster_url为：%s" % poster_url)
                    logger.info(u"poster_url为：%s" % poster_url)
                    # cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
                    #
                    #
                    # real_path_no = os.path.join(cur_path, "jpg/bv-%s-%s.png" % (str_time, title))
                    # self.driver.get_screenshot_as_file(real_path_no)
                    self.bf.get_circle_screen_shot(title,waittime,count_c)

                    download = self.driver.find_element_by_id("download")
                    download.click()
                    self.driver.implicitly_wait(3)

                    self.driver.switch_to_default_content()
                    offer_id = self.driver.find_element_by_id("info").text
                    print(u"offer_id为：%s" % offer_id)
                    logger.info(u"offer_id为：%s" % offer_id)

                    all_windows = self.driver.window_handles
                    if len(all_windows) == 2:
                        print(u"%s:点击跳转成功" % title)
                    else:
                        print(u"%s:点击跳转成功" % title)

                    # self.driver.switch_to_window(all_windows[1])
                    print(self.driver.current_url)

                    # self.driver.implicitly_wait(3)
                    # self.driver.switch_to_window(all_windows[0])
                    # self.driver.implicitly_wait(1)
                    # real_path_yes = os.path.join(cur_path, "jpg/yes-%s-%s.png" % (str_time, title))
                    # print(real_path_yes)

                    # self.driver.get_screenshot_as_file(real_path_yes)
                    # self.driver.fullscreen_window()
                    self.driver.quit()
                else:
                    print(u"无offer")
                    self.driver.quit()


            except Exception as msg:
                print(u"异常信息---%s" % msg)
                self.driver.quit()







if __name__ == "__main__":
    # url = "https://pingan.i99pay.com/Public/bv.html"
    # jd = jssdk_bv()
    # jd.get_loc(url)

    count=2
    for i in range(count):
        url = "http://interactive.mintegral.com/qa_task/t253/v4/jssdk_830137/h/bv.html"
        jd = jssdk_bv()
        jd.get_loc(url,3,5)

















