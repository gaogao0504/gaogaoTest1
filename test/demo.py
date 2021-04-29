# a=1
# def demo1():
#     #告诉解释器使用外面的全局的a
#     global a
#     a=2 #方法内的变量赋值大于方法外自定义的变量赋值 但是需要方法内自己使用
#     print(a) #打印取最近的值
#     print(id(a))
#     # 定义函数没有任何函数值，默认会返回一个none
#     return a
#
# print(demo1())
# print(a)
# print(id(a))
#
# #支持嵌套函数，闭包函数
# def outer():
#     def inner():
#         print('inner')
#     return inner
# outer()


# pytest的安装
# pip3 install pytest
# pytest --version
# pytest执行命令
# 1、绿色的点为pass
# 2、红色的f是fail
# 3、红色的e为errao
#
# 4、pytest 运行方式
# -s 将print的信息打印出来
# -v 打印详细文件
# pytest --help 查看命令的使用信息
# pytest -vs 知道执行的那个文件以及方法或者类的详细信息
# pytest -vs 文件名 执行某一个文件
# pytest - vs 文件名::test_a 执行某一个文件下的某一个方法
# pytest - vs 文件名::TestDEMO::test_case1 执行某一个文件下一个类下的一个方法
# pytest -x 一旦失败报错就停止
# pytest --maxfail= num      允许失败几条还可以执行
# pytest -k "" 执行某一条含有关键词的测试用例
# pytest -m  加标记
# --lf 执行失败的用例
# --ll 优先执行失败的用例


# 界面操作
# pycharm preferences
# a =1
# b =2
#
# def func():
#     print(a+b)
#
# print(a)
# func()
# print(b)

# yield用法
# 生成器

# 安装allure2 brew install allure
# 安装allure_pytest
# pytest test_cal1.py --alluredir ./result
# allure serve ./result


# 什么是html 超文本标记语言，描述网页的语言，
# 控制台开发者工具 elements
# html基本结构
# 像浏览器声明这是一个html语言 <!DOCTYPE html>
# 根标签 <html>
# 写给浏览器看的标签<head>
# 设置当前网页显示的编码 <body>
# 设置当前网页的标题 <title>
# 网页的主体，显示在浏览器空白的页面<>
# html的基本标签
#   双标签：<标签名></标签名>
#   单标签：<标签名/>
# 标签的属性
# 标签可以拥有多个属性


# html全局属性
# class 规定元素的类名
# id：
# lang：
# stytle：
#
#
#
#
# 事件属性
import  selenium


#


def provider():
    for i in range(0, 10):
        print('start')
        yield i
        # 相当于return，用来返回数据，记录了上一吃的执行位置，下一次继续执行
        print('end')


p = provider()
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))



print(provider())
