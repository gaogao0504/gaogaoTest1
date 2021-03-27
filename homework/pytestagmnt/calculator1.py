"""
1、补全计算器（加法，除法）的测试用例
2、使用数据驱动完成测试用例的自动生成
3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
坑1:除数为0的情况
坑2: 自己发现
"""


# 被测试代码 实现计算器功能


class Calculator:

    # 相加功能
    def add(self, a, b):
        return a + b

    # 相减功能
    def sub(self, a, b):
        return a - b

    # 相乘功能
    def multi(self, a, b):
        return a * b

    # 相除功能
    def div(self, a, b):
        # if b == 0:
        #     print("0")
        # else:
        #     return a / b

        try:
            return a / b
        except Exception as e:
            return "这里有个异常"
