# conftest开发公共模块
import pytest

from pythoncode import Calculator


@pytest.fixture()
def get_calc():
    print('开始计算')
    calc = Calculator()
    yield calc
    print('结束计算')