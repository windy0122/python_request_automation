import unittest
from math_method import MathMethod


class TestMathMethod(unittest.TestCase):

    def test_add_two_one(self):
        res = MathMethod(1, 1).add()
        print("1+1的结果是：", res)
        try:
            self.assertEqual(1, res, '算法错误')
        except AssertionError as e:
            print('错误啦，断言错误{0}'.format(e))
            raise e

    def test_add_two_zero(self):
        res = MathMethod(0, 0).add()
        print("0+0的结果是：", res)

    def test_add_two_negative(self):
        res = MathMethod(-1, -2).add()
        print("-1+-2的结果是：", res)


if __name__ == '__main__':
    unittest.main()


