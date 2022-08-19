import unittest
from time import sleep
from selenium import webdriver
from page_object.index_page import IndexPage
from page_object.login_page import LoginPage
from ddt import ddt, file_data, data, unpack
from config.yamlload import loadyaml

# 设计测试用例
@ddt
class TestCase(unittest.TestCase):

    # 初始化浏览器
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
        cls.sec = IndexPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @file_data('../data/user.yaml')
    def test_1_login(self, user, pwd):
        txt = self.lp.login(user, pwd)
        sleep(2)
        # self.assertEqual(txt,ttt) 断言

    @data('11', '55')
    def test_2_login(self, txt):
        self.sec.select(txt)
        sleep(2)


if __name__ == '__main__':
    unittest.main()
