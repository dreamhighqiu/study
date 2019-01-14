#需要安装客户端的包
#pip3 install Appium-Python-Client
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import multiprocessing

def get_driver(device,port):
    cap = {
        "platformName": "Android",
        "platformVersion": "4.4.2",
        "deviceName": device,
        'udid':device,
        "appPackage": "com.tal.kaoyan",
        "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
        "noReset": True
    }

    driver = webdriver.Remote("http://localhost:%d/wd/hub"%port, cap)

    init_app(driver)

    login(driver)
    get_yanxun(driver)
    get_size(driver)
    login_out(driver)
def init_app(driver):
    try:
        # 是否跳过
        if WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(
                "//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_skip']")):
            driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_skip']").click()
    except:
        pass


    try:
        # 隐私协议
        if WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(
                "//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_title']")):
            driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_agree']").click()
            driver.find_element_by_xpath(
                "//android.support.v7.widget.RecyclerView[@resource-id='com.tal.kaoyan:id/date_fix']/android.widget.RelativeLayout[3]").click()
    except:
        pass


def get_yanxun(driver):

    # 点击研讯
    if WebDriverWait(driver, 3).until(lambda x: x.find_element_by_xpath(
            "//android.support.v7.widget.RecyclerView[@resource-id='com.tal.kaoyan:id/date_fix']/android.widget.LinearLayout[2]")):
        driver.find_element_by_xpath(
            "//android.support.v7.widget.RecyclerView[@resource-id='com.tal.kaoyan:id/date_fix']/android.widget.LinearLayout[2]").click()
def login(driver):
    if WebDriverWait(driver, 3).until(
            lambda x: x.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_mysefl")):
        driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
    if WebDriverWait(driver, 3).until(
            lambda x: x.find_element_by_id("com.tal.kaoyan:id/activity_usercenter_logintip_img")):
        driver.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_logintip_img').click()


    try:
        if WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(
                "//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_email_edittext']")):
            driver.find_element_by_xpath(
                "//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_email_edittext']").send_keys(
                "dazhuang123")
            driver.find_element_by_xpath(
                "//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_password_edittext']").send_keys(
                "qwe123asd")
            driver.find_element_by_xpath(
                "//android.widget.Button[@resource-id='com.tal.kaoyan:id/login_login_btn']").click()
    except:
        pass
    if WebDriverWait(driver, 3).until(
            lambda x: x.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_calendar")):
        driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_calendar').click()

def get_size(driver):
    x = int(driver.get_window_size()['width'])
    y = int(driver.get_window_size()['height'])
    x1 = int(x * 0.5)
    y1 = int(y * 0.75)
    y2 = int(y * 0.25)

    # 滑动操作
    i = 10
    while i > 0:
        driver.swipe(x1, y1, x1, y2)
        time.sleep(0.5)
        i = i - 1


def login_out(driver):
    # 点击返回
    if WebDriverWait(driver, 3).until(
            lambda x: x.find_element_by_id("com.tal.kaoyan:id/myapptitle_leftbutton_wraper")):
        driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_leftbutton_wraper').click()
    # 点击我的
    driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
    if WebDriverWait(driver, 3).until(
            lambda x: x.find_element_by_id("com.tal.kaoyan:id/myapptitle_RightButton_textview")):
        driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_RightButton_textview').click()
    # 点击设置
    if WebDriverWait(driver, 3).until(lambda x: x.find_element_by_id("com.tal.kaoyan:id/setting_logout_text")):
        driver.find_element_by_id('com.tal.kaoyan:id/setting_logout_text').click()
    # 退出登录
    if WebDriverWait(driver, 3).until(lambda x: x.find_element_by_id("com.tal.kaoyan:id/tip_commit")):
        driver.find_element_by_id('com.tal.kaoyan:id/tip_commit').click()


if __name__ == "__main__":
    m_list=[]
    devices_list=['127.0.0.1:62001','127.0.0.1:62025']
    for device in range(len(devices_list)):
        port=4723+2*device
        m_list.append(multiprocessing.Process(target=get_driver,args=(devices_list[device],port,)))
    for m1 in m_list:
        m1.start()
    for m2 in m_list:
        m2.join()




