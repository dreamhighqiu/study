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
from jssdk_video.util.logger import Logger
from jssdk_video.base.base import base_func
logger = Logger(logger="jssdk_nv").getlog()

class jssdk_nv():
    def __init__(self):
        #chrome浏览器wap方式打开，无手机属性，不需要切换上下文
        mobile_emulation = {"deviceName": "iPhone 6"}
        options = Options()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        #Chrome正在受到自动软件的控制
        options.add_argument("disable-infobars")
        #静默模式打开浏览器不依赖前端页面
        options.add_argument("headless")
        self.driver = webdriver.Chrome(chrome_options=options)
        self.bf = base_func(self.driver)
        # --ignore-certificate-errors.稳定性和安全性会有所下降（解决方式）
        # https://www.cnblogs.com/yoyoketang/p/6789537.html
    def get_loc(self,url,waittime,count_c):
        self.driver.get(url)
        self.driver.implicitly_wait(3)
        result = self.driver.find_element_by_id("mvvideobannerplayer")
        if not result:
            print(result.text)
        else:
            print(u"接口有返回广告")
            #滑动浏览器屏幕
            self.driver.execute_script("window.scrollBy(0,4000)")
            try:
                # 获取当前的时间
                str_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(int(time.time())))
                self.driver.implicitly_wait(3)

                mvvideobannerplayer = self.driver.find_element_by_id("mvvideobannerplayer")

                #untill 间隔获取定位元素
                element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id("title"))

                # ec 间隔获取定位元素
                # element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "title")))
                title = element.text
                logger.info(u"----%soffer广告信息为--%r--" % (title, str_time))
                print(u"offer标题为:%s" % title)
                logger.info(u"offer标题为:%s" % title)
                video = self.driver.find_element_by_tag_name("video").get_attribute("src")
                logger.info(u"offer的视频内容:%s"% video)
                print(u"offer的视频内容:%s" % video)

                poster_url = self.driver.find_element_by_id("mvvideobannerplayer").get_attribute(
                    "poster")
                print(u"poster_url为：%s" % poster_url)
                logger.info(u"poster_url为：%s" % poster_url)
                #获取iframe定位，定位iframe内的元素
                frame = self.driver.find_element_by_xpath("//div/iframe")
                self.driver.switch_to_frame(frame)
                self.driver.implicitly_wait(5)
                #切出iframe框架
                #self.driver.switch_to_default_content()


                if mvvideobannerplayer:
                    icon = self.driver.find_element_by_id("icon").get_attribute("src")
                    print(u"offer的icon为：%s" % icon)
                    logger.info(u"offer的icon为：%s" % icon)

                    self.driver.implicitly_wait(5)

                    notice_url = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/a").get_attribute(
                        "notice")
                    print(u"notice_url为：%s" % notice_url)
                    logger.info(u"notice_url为：%s" % notice_url)
                    click_url = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/a").get_attribute(
                        "click")
                    print(u"click_url为：%s" % click_url)
                    logger.info(u"click_url为：%s" % click_url)
                    href_url = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/a").get_attribute(
                        "href")
                    print(u"href_url为：%s" % href_url)
                    logger.info(u"href_url为：%s" % href_url)
                    agentclick_url = self.driver.find_element_by_xpath(
                        "/html/body/div[2]/div[1]/div[3]/a").get_attribute(
                        "agentclick")
                    print(u"agentclick_url为：%s" % agentclick_url)
                    logger.info(u"agentclick_url为：%s" % agentclick_url)
                    campaignid = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/a").get_attribute(
                        "campaignid")
                    print(u"campaignid为：%s" % campaignid)
                    logger.info(u"campaignid为：%s" % campaignid)


                    # cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
                    #
                    #
                    # real_path_no = os.path.join(cur_path, "jpg/nv-%s-%s.png" % (str_time, title))
                    # self.driver.get_screenshot_as_file(real_path_no)
                    self.bf.get_circle_screen_shot(title,waittime,count_c)

                    self.driver.switch_to_default_content()
                    download = self.driver.find_element_by_id("download")
                    download.click()
                    self.driver.implicitly_wait(3)
                    # offer_id = self.driver.find_element_by_id("info").text
                    # print(u"offer_id为：%s" % offer_id)

                    all_windows = self.driver.window_handles
                    if len(all_windows) == 2:
                        print(u"%s:点击跳转成功" % title)
                    else:
                        print(u"%s:点击跳转成功" % title)
                    print(self.driver.current_url)
                    self.driver.quit()

                else:
                    print(u"无offer")
                    self.driver.quit()
                #获取所有的窗口句柄
                #all_windows = self.driver.window_handles
                # self.driver.current_window_handle  获取当前的句柄
                #切换到其他的句柄
                # self.driver.switch_to_window(all_windows[1])


            except Exception as msg:
                print(u"异常信息---%s" % msg)
                # self.driver.quit()




if __name__ == "__main__":
    # url = "https://pingan.i99pay.com/Public/nv.html"
    # jd = jssdk_nv()
    # jd.get_loc(url)

    count=2
    for i in range(count):
        url = "http://interactive.mintegral.com/qa_task/t253/v4/jssdk_830137/h/nv.html"
        jd = jssdk_nv()
        jd.get_loc(url,3,5)

















