


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
# PO页面对象

# 复用浏览器，只对当前页面做操作
from selenium import webdriver


class TestWework:

    def test_addmember(self):
        opt = webdriver.ChromeOptions()
        # 设置debug地址
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(10)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        driver.find_element_by_id("menu_contacts").click()
        # 调试driver
        ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        # 显示等待
        # WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(ele))
        # driver.find_element_by_css_selector(".ww_operationBar .js_add_member").click()
        while True:
            # *ele解元组
            driver.find_element(*ele).click()
            ele_num = len(driver.find_elements(By.ID, "username"))
            if ele_num > 0:
                break
        driver.find_element_by_id("username").send_keys("高高1")
        driver.find_element_by_id("memberAdd_acctid").send_keys("0426")
        driver.find_element_by_id("memberAdd_phone").send_keys("18103518661")
        driver.find_element_by_css_selector(".js_btn_save").click()
        eles = driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(5)")
        print(eles)
        for value in eles:
            if value.get_attribute("title") == "18103518661":
                return True

