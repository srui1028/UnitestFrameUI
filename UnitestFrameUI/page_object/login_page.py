'''
    LoginPage类，专门用户实现登录页面对象的文件
    主体内容包含：
        1、核心的页面元素
            账号，密码，登录按钮
        2、核心的业务流
            用户的登录行为
'''
from time import sleep
from selenium import webdriver
from base.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    # 核心元素
    url = "http://10.20.17.211:30000/"

    #选择系统账号登录
    # choic = (By.XPATH, '//*[@id="userLayout"]/div/div/div[2]/div/div/div[2]/label[2]/span[2]')
    user = (By.XPATH, "//input[contains(@placeholder,'请输入系统账号')]")
    pwd = (By.XPATH, "//input[contains(@placeholder,'请输入密码')]")
    login_button = (By.XPATH, "//button[@type='submit'][contains(.,'登 录')]")

    # 核心业务流
    def login(self, user, pwd):
        self.visit()
        max_window = self.driver.maximize_window()
        sleep(3)
        # self.click(self.choic)
        self.input(self.user, user)
        self.input(self.pwd, pwd)
        sleep(2)
        self.click(self.login_button)
        sleep(3)
        # 添加一个返回值，用户获取断言的文本信息



# 调试代码
# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     user = "admin"
#     pwd = "admin"
#     lp = LoginPage(driver)
#     lp.login(user, pwd)


