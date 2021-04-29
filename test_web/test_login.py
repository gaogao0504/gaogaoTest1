from selenium import webdriver


class TestLogin:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").click()
        self.driver.find_element_by_id("kw").send_keys("霍格沃兹测试学院")
        self.driver.find_element_by_id("su").click()
        # 找到目标元素，赋值给ele
        ele = self.driver.find_element_by_link_text("霍格沃兹测试学院 – 软件自动化测试开发培训_接口性能测试")
        assert ele

# 复用浏览器步骤
# 1、关闭全部的浏览器
# 2、配置chrome的环境变量
#    vim ~/.bash_profile
#    export PATH=$PATH:[chromedriver所在路径]
#    export PATH=/Applications/Google\ Chrome.app/Contents/MacOS:$PATH
#    mac配置完成后，需要重新加载环境变量
#    source ~ /.bash_profile
#      查看环境变量是否生效
#     witch $chromedriver
# 2、Goole\ 如找到环境变量则用次命令Chrome --remote-debugging-port=9222
# 3、找不到此命令用 /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
