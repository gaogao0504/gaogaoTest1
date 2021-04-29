from time import sleep
from selenium import webdriver
import pytest


class TestA:

    def setup(self):
        self.driver = webdriver.Chrome("/usr/local/bin/ChromeDriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_a(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("求职面试圈").click()
        self.driver.find_elements_by_name("一线大厂软件测试流程（思维导图）详解").click()



