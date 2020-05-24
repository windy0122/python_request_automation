import unittest
from class_unittest.class_unittest_one import TestMathMethod
import HTMLTestRunner_cn


# 方法1 test suite
suite = unittest.TestSuite()

# suite.addTest(TestMathMethod('test_add_two_one'))
# suite.addTest(TestMathMethod('test_add_two_zero'))
# suite.addTest(TestMathMethod('test_add_two_negative'))
#


# 方法2  test loader
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestMathMethod))

# report_file = open('test.txt', 'w+', encoding='UTF-8')
# with open('test.txt', 'w+', encoding='UTF-8') as report_file:
#     runner = unittest.TextTestRunner(stream=report_file, verbosity=2)
#     runner.run(suite)

# HTMLTestRunner测试报告
with open('test_report.html', 'wb') as file:
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=file, verbosity=2,
                                              title="迪哥的测试报告", description="第一次报告", tester="迪哥")
    runner.run(suite)
