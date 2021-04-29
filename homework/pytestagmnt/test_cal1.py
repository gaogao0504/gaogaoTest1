"""
1、补全计算器（加法，除法）的测试用例
2、使用数据驱动完成测试用例的自动生成
3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
坑1:除数为0的情况
坑2: 自己发现
"""
import pytest

from pythoncode.homework.pytestagmnt.calculator1 import Calculator


class TestCal:
    # 测试相加功能
    def setup_method(self):
        print("开始计算")

    def teardown_method(self):
        print("计算结束")

    # 测试相加功能
    @pytest.mark.parametrize("a, b, expect",
                             [[1, 2, 3], [1, 2, 4], [0.1, 0.1, 0.2], [0.1, 0.2, 0.8], [1, -1, 9], [1, -2, 1],
                              [-1, -2, -3], [-1, -2, -4], [0, 0, 0]])
    def test_add(self, a, b, expect):
        calc = Calculator()
        assert calc.add(a, b) == expect

    # 测试相减功能
    @pytest.mark.parametrize("a, b, expect",
                             [[1, 2, -1], [5, 2, 2], [0.8, 0.1, 0.7], [0.1, 0.2, 0.8], [1, -1, 2], [1, -2, 1],
                              [-1, -2, 1], [-1, 2, -3], [0, 0, 0]])
    def test_sub(self, a, b, expect):
        calc = Calculator()
        assert calc.sub(a, b) == expect

    # 测试相乘功能
    @pytest.mark.parametrize("a, b, expect",
                             [[1, 2, 2], [1, 2, 4], [0.1, 0.1, 0.01], [0.1, 0.2, 0.8], [1, -1, -1], [1, -2, 1],
                              [-1, -2, 2], [-1, -2, -4], [0, 0, 0]])
    def test_multi(self, a, b, expect):
        calc = Calculator()
        assert calc.multi(a, b) == expect

    # 测试相除功能
    @pytest.mark.parametrize("a, b, expect",
                             [[1, 2, 0.5], [1, 2, 4], [0.1, 0.1, 1], [0.1, 0.2, 0.8], [1, -1, -1], [1, -2, 1],
                              [-1, -2, 0.5], [-1, -2, -4], [0, 1, 0], [1, 0, 0]])
    def test_div(self, a, b, expect):
        calc = Calculator()
        try:
            calc.div(a, b)

        except Exception as e:
            print("这里有个异常")

        else:
            assert calc.div(a, b) == expect

