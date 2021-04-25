from time import sleep

import yaml
from selenium import webdriver


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


# 复用浏览器，只对当前页面做操作
class TestWework:

    def test_login(self):
        opt = webdriver.ChromeOptions()
        # 设置debug地址
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(10)
        driver.find_element_by_id("menu_contacts").click()
        # 获取cookies
        # print(driver.get_cookies())
        cookie = driver.get_cookies()
        with open("data.yaml", "w", encoding="UTF-8") as f:
            yaml.dump(cookie, f)

    # # 复用cookies版本1
    # def test_cookies(self):
    #     driver = webdriver.Chrome()
    #     driver.get("https://work.weixin.qq.com/")
    #     cookies = [
    #         {'domain': '.qq.com', 'expiry': 1619314840, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
    #          'value': '1'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False,
    #          'value': ''},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
    #          'value': '1688851244948589'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
    #          'value': 'DBgoa3XFe8eAqrhKINAXNeXBZRRTRXThhXTbmjFI0YRN_i5dGDMM82xXiBAObBEXKS-wQuof5H3aJdN-qNGyY5wjEYHNi2dG9kkfeqiSbbsz7eB7v__TvfF2M6SIgJCREFtuRmmUBrtrwFWL-s-oorFFs49E6SYXkmwtXHn-ma-F2N-ayqJOnf5TGsNlOThI40xwuzyglWCEdtcfwo4Ysn0Wa3dvi2mQZ9p-d0EOrEK0mWghjK6upZn20PYFEVbjsmJ3Cm43Y6pHqV_JFdz5ew'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
    #          'value': '1688851244948589'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
    #          'value': '1970325016440198'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
    #          'value': 'KrOawuhucAvCFasZFDIlPvhEIV3Ji-s_sr9HFvuQR_-rcIcWNIvC_OW8brgmcqBo'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
    #          'value': 'a871273'},
    #         {'domain': '.qq.com', 'expiry': 1619400777, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
    #          'value': 'GA1.2.1594295435.1619314367'},
    #         {'domain': 'work.weixin.qq.com', 'expiry': 1619345902, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
    #          'secure': False, 'value': '40t16bn'},
    #         {'domain': '.qq.com', 'expiry': 1682386377, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
    #          'value': 'GA1.2.1557065433.1618462241'},
    #         {'domain': '.work.weixin.qq.com', 'expiry': 1649998239, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
    #          'path': '/', 'secure': False, 'value': '0'},
    #         {'domain': '.qq.com', 'expiry': 1620825419, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/',
    #          'secure': False, 'value': '839479743@qq.com'},
    #         {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
    #          'value': 'c8200c39ed4e760d607e6a0301d4a73ed6baa475192d3665aea700c2cab64d8b'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
    #          'value': '11258394741966158'},
    #         {'domain': '.qq.com', 'expiry': 1932094290, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
    #          'secure': False, 'value': '8e5c46c1466b90c3'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
    #          'value': '1'},
    #         {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
    #          'secure': False, 'value': '3963583750'},
    #         {'domain': '.work.weixin.qq.com', 'expiry': 1650033127, 'httpOnly': False,
    #          'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
    #          'value': '1618462240,1618497127'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
    #          'value': 'direct'},
    #         {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
    #          'value': 'rRhgKYrOdn'},
    #         {'domain': '.work.weixin.qq.com', 'expiry': 1621906380, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
    #          'path': '/', 'secure': False, 'value': 'zh'}]
    #
    #     for cookie in cookies:
    #         # 把cookie计入driver内
    #         driver.add_cookie(cookie)
    #     driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    #     sleep(5)

    def test_cookie_v2(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        # 打开二维码页面
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        with open("data.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        sleep(10)
