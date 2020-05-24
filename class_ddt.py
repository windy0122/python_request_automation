import unittest
from ddt import ddt, data, unpack


# test_data = [[1, 2, 3], [4, 5, 6]]

test_data = [{'name': 'windy', 'language': 'python'}, {'name': 'what', 'language': 'java'}]


@ddt
class TestMath(unittest.TestCase):
    @data(*test_data)  # 装饰测试方法，拿到几个数据，就执行几条用例
    # @unpack
    # 在用*test_data的同时，将拿到的参数进行拆分，[1,2,3]-->1,2,3同时需要用3个参数来接收，(self, a,b,c)
    # 如果unpack后的参数少于5个，推荐用unpack，要注意参数不对等的情况，提供对应参数来接收变量
    def test_print_data(self, a):
        print(a)
        # print(b)
        # print(c)
        # print(name)
        # print(language)
