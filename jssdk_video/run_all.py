# coding:utf-8
import unittest
import os
import time
import HTMLTestRunner_jpg
from util.send_mail_file import Send_Mail_file
from config import ParseConfigurationFile

# python2.7要是报编码问题，就加这三行，python3不用加
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
# sys.path.append('E:\\tools')
#run_case文件放项目run_case目录
# cur_path = os.path.dirname(os.getcwd())
# print cur_path

#run_case文件放项目根目录
cur_path=os.path.dirname(__file__)
print(cur_path)
# 测试用例的路径
case_path = os.path.join(cur_path, "case")


# 设置报告文件存路径
report_path = os.path.join(cur_path, "report/")
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
# 设置报告名称格式
HtmlFile = report_path + now + "HtmlReport.html"
fp = open(HtmlFile, "wb")

def run_main():
    discover = unittest.defaultTestLoader.discover(case_path, "test*.py")
    run = HTMLTestRunner_jpg.HTMLTestRunner(title=u"jssdk_demo测试报告", description=u"综述", stream=fp)
    run.run(discover)

    # run_case文件放项目run_case目录
    # cur_path = os.path.dirname(os.getcwd())

    # run_case文件放项目根目录
    cur_path = os.path.dirname(__file__)
    report_path = os.path.join(cur_path, "report")  # 用例文件夹

    mail = Send_Mail_file()
    report_file = mail.get_report_file(report_path)  # 3获取最新的测试报告
    pc = ParseConfigurationFile.ParseConfigfile()
    sender = pc.getOptionValue("email", "sender")
    psw = pc.getOptionValue("email", "psw")
    smtp_server = pc.getOptionValue("email", "smtp_server")
    port = pc.getOptionValue("email", "port")
    receiver = pc.getOptionValue("email", "receiver")
    mail.send_mail(sender, psw, receiver, smtp_server, report_file, port)  # 4最后一步发送报告


if __name__ == "__main__":
    run_main()












