# _*_ coding: utf-8 _*_
import logging
import os.path
import time


class Logger_new(object):
    def __init__(self, logger):
        '''''
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        '''

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # log_path = os.path.dirname(os.getcwd()) + '/Logs/'  # 项目根目录下/Logs 保存日志
        #log_path = os.path.dirname(os.path.abspath('.')) + '/log/'
        log_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/log/'

        # 如果case组织结构式 /testsuit/featuremodel/xxx.py ， 那么得到的相对路径的父路径就是项目根目录
        log_name = log_path + rq + '.log'

        fh_new = logging.FileHandler(log_name)
        fh_new.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch_new = logging.StreamHandler()
        ch_new.setLevel(logging.INFO)

        # 定义handler的输出格式
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatter = logging.Formatter('%(message)s')
        fh_new.setFormatter(formatter)
        ch_new.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh_new)
        self.logger.addHandler(ch_new)
    def getlog(self):
        return self.logger