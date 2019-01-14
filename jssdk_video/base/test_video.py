# -*- coding: utf-8 -*-
'''
Created on ：2018/7/25:11:43

@author: yunxia.qiu
'''
from jssdk_video.base.base import base_func
from jssdk_video.util.logger import Logger
import unittest
from selenium.webdriver.support.wait import WebDriverWait
import os,time
from ddt import ddt,data,unpack
logger = Logger(logger="bv").getlog()

@ddt
class video(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.bf =base_func()
        cls.driver = cls.bf.launch_chrome()
    # def setUp(self):
    #     self.bf = base_func()
    #     self.driver = self.bf.launch_chrome()


    def bv(self,url):
        self.driver.implicitly_wait(3)

        self.driver.get(url)
        try:
            self.driver.implicitly_wait(5)
            frame = self.driver.find_element_by_xpath("//div/iframe")
            self.driver.switch_to_frame(frame)
            self.driver.implicitly_wait(3)
            mvvideobannerplayer = self.driver.find_element_by_id("mvvideobannerplayer")
            if mvvideobannerplayer:
                element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id("title"))

                # element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "title")))
                title = element.text
                print(u"offer标题为:%s" % title)
                icon = self.driver.find_element_by_id("icon").get_attribute("src")
                print(u"offer的icon为：%s" % icon)
                video = self.driver.find_element_by_tag_name("video").get_attribute("src")
                print(u"offer的视频内容:%s" % video)
                notice_url = self.driver.find_element_by_xpath("//*[@id='info_warp']").get_attribute("notice")
                print(u"notice_url为：%s" % notice_url)
                click_url = self.driver.find_element_by_xpath("//*[@id='info_warp']").get_attribute("click")
                print(u"click_url为：%s" % click_url)
                href_url = self.driver.find_element_by_xpath("//*[@id='info_warp']").get_attribute("href")
                print(u"href_url为：%s" % href_url)
                agentclick_url = self.driver.find_element_by_xpath("//*[@id='info_warp']").get_attribute(
                    "agentclick")
                print(u"agentclick_url为：%s" % agentclick_url)
                cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
                str_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(int(time.time())))

                real_path_no = os.path.join(cur_path, "jpg/bv-%s-%s.png" % (str_time, title))
                self.driver.get_screenshot_as_file(real_path_no)

                download = self.driver.find_element_by_id("download")
                download.click()
                self.driver.implicitly_wait(3)

                self.driver.switch_to_default_content()
                offer_id = self.driver.find_element_by_id("info").text
                print(u"offer_id为：%s" % offer_id)

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
                # self.driver.quit()
            else:
                print(u"无offer")
                # self.driver.quit()


        except Exception as msg:
            print(u"异常信息%s" % msg)
            # self.driver.quit()
    def nv(self,url):
        self.driver.implicitly_wait(3)
        self.driver.get(url)
        self.driver.implicitly_wait(3)
        self.driver.execute_script("window.scrollBy(0,4000)")
        try:
            self.driver.implicitly_wait(3)

            mvvideobannerplayer = self.driver.find_element_by_id("mvvideobannerplayer")
            video = self.driver.find_element_by_tag_name("video").get_attribute("src")
            print(u"offer的视频内容:%s" % video)
            element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id("title"))

            # element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "title")))
            title = element.text
            print(u"offer标题为:%s" % title)
            frame = self.driver.find_element_by_xpath("//div/iframe")
            self.driver.switch_to_frame(frame)
            self.driver.implicitly_wait(5)

            if mvvideobannerplayer:

                icon = self.driver.find_element_by_id("icon").get_attribute("src")
                print(u"offer的icon为：%s" % icon)

                self.driver.implicitly_wait(5)

                notice_url = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/a").get_attribute(
                    "notice")
                print(u"notice_url为：%s" % notice_url)
                click_url = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/a").get_attribute(
                    "click")
                print(u"click_url为：%s" % click_url)
                href_url = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/a").get_attribute("href")
                print(u"href_url为：%s" % href_url)
                agentclick_url = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/a").get_attribute(
                    "agentclick")
                print(u"agentclick_url为：%s" % agentclick_url)
                campaignid = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/a").get_attribute(
                    "campaignid")
                print(u"campaignid为：%s" % campaignid)

                cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
                str_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(int(time.time())))

                real_path_no = os.path.join(cur_path, "jpg/nv-%s-%s.png" % (str_time, title))
                self.driver.get_screenshot_as_file(real_path_no)

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
                # self.driver.quit()
            else:
                print(u"无offer")
                # self.driver.quit()


        except Exception as msg:
            print(u"异常信息%s" % msg)
            # self.driver.quit()
    # @unittest.skip
    @data(2)
    def test_bv(self,count):
        # count = 2
        for i in range(count):
            url_bv = "https://pingan.i99pay.com/Public/bv.html"
            self.bv(url_bv)
    @unittest.skip
    @data(2)
    def test_nv(self,count):
        # count = 1
        for i in range(count):
            url_nv = "https://pingan.i99pay.com/Public/nv.html"
            self.bv(url_nv)

    @classmethod
    def tearDownClass(cls):
        cls.bf.close_chrome()
        # cls.bf =base_func()
        # cls.bf.close_chrome()
    # def tearDown(self):
    #     self.bf.close_chrome()


if __name__ == "__main__":
    unittest.main()










