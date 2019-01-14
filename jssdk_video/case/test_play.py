# -*- coding: utf-8 -*-
'''
Created on ：2018/7/25:13:38

@author: yunxia.qiu
'''
import sys
sys.path.append("E:\\tools")

from jssdk_video.base.base import base_func
from jssdk_video.util.logger import Logger
import unittest
from jssdk_video.base.start_jssdk_bv import jssdk_bv
from jssdk_video.base.start_jssdk_nv import jssdk_nv
from jssdk_video.base.start_jssdk_fv import jssdk_fv
from selenium.webdriver.support.wait import WebDriverWait
import os,time
from ddt import ddt,data,unpack
# logger = Logger(logger="bv").getlog()

class test_case(unittest.TestCase):

    def test_bv(self):

        count = 2
        waittime = 3
        count_c = 4
        for i in range(count):
            url_bv = "http://interactive.mintegral.com/qa_task/t253/v4/jssdk_830137/h/bv.html"
            jd = jssdk_bv()
            jd.get_loc(url_bv,waittime,count_c)

    def test_nv(self):

        count = 2
        waittime = 3
        count_c = 4
        for i in range(count):
            url_nv = "http://interactive.mintegral.com/qa_task/t253/v4/jssdk_830137/h/nv.html"
            jd = jssdk_nv()
            jd.get_loc(url_nv,waittime,count_c)

    def test_fv(self):

        count=2
        waittime =3
        count_c =4
        for i in range(count):
            url_fv ="http://interactive.mintegral.com/qa_task/t253/v4/jssdk_830137/h/fv.html"
            jd= jssdk_fv()
            jd.get_loc(url_fv,waittime,count_c)


if __name__ == "__main__":
    unittest.main()