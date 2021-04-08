"""
1、补全计算器（加法，除法）的测试用例
2、使用数据驱动完成测试用例的自动生成
3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
坑1:除数为0的情况
坑2: 自己发现
"""
import pytest
import yaml

from pythoncode.homework.pytestagmnt_test.calculator1 import Calculator


def get_datas():
    with open("pyagment.yaml") as f:
        datas = yaml.safe_load(f)
    return datas


# def test_datas():
#     test_add = get_datas()['test_add']
#     test_sub = get_datas()['test_sub']
#     test_multi = get_datas()['test_multi']
#     test_div = get_datas()['test_div']
#     print(test_add)
#     print(test_sub)
#     print(test_multi)
#     print(test_div)


class TestCal:
    # 测试相加功能
    # def setup_method(self):
    #     print("开始计算")

    # def teardown_method(self):
    #     print("计算结束")
    #
    # def setup(self):
    #     self.calc = Calculator()
    #     print("准备开始计算")

    # 测试相加功能
    @pytest.mark.parametrize('a,b,expect', get_datas()['test_add']['datas'], ids=get_datas()['test_add']['ids'])
    def test_add(self, get_calc, a, b, expect):
        assert get_calc.add(a, b) == expect

    # 测试相减功能
    @pytest.mark.parametrize('a,b,expect', get_datas()['test_sub']['datas'], ids=get_datas()['test_sub']['ids'])
    def test_sub(self, get_calc, a, b, expect):
        # 保留两位小数round
        assert round(get_calc.sub(a, b), 2) == expect

    # 测试相乘功能
    @pytest.mark.parametrize('a,b,expect', get_datas()['test_multi']['datas'], ids=get_datas()['test_multi']['ids'])
    def test_multi(self, get_calc, a, b, expect):
        assert get_calc.multi(a, b) == expect

    # 测试相除功能
    @pytest.mark.parametrize('a,b,expect', get_datas()['test_div']['datas'], ids=get_datas()['test_div']['ids'])
    def test_div(self, get_calc, a, b, expect):
        # 异常处理机制，捕获异常
        with pytest.raises(ZeroDivisionError):
            get_calc.div(a, b)

        # try:
        #     self.calc.div(a, b)
        # except Exception as e:
        #     print("除数为0")
        # else:
        #     assert calc.div(a, b) == expect
