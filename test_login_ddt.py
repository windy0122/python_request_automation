import requests
from ddt import ddt, data, unpack
import unittest
from get_data import GetData
import json
import HTMLTestRunner_cn


test_data = GetData('test.xlsx', 'Sheet1').get_data()

uat_url = 'https://uatleague.round-table-union.com/api/rts/base/home/login/v110'

header = {
    'content-type': 'application/json',
    'version': '1.3.1',
    'platform': 'iOS'
}


@ddt
class LoginTest(unittest.TestCase):

    @data(*test_data)
    @unpack
    def test_login(self, login_code, password):
        payload = {
            "smsCodeToken": '',
            "standbyUniqueIdentification": "_Android10",
            "deviceUniqueIdentification": "",
            "password": password,
            "loginType": "1",
            "smsCode": '',
            "loginCode": login_code,
            "source": "",
            "applicationId": "AoSf3sOaLVENjofVUhIoMRt-Pjs7603WuGNytkwvoC2y"
        }

        r = requests.post(url=uat_url, headers=header, data=json.dumps(payload), verify=False)
        print(r.json())


suite = unittest.TestSuite()
loder = unittest.TestLoader()
suite.addTest(loder.loadTestsFromTestCase(LoginTest))

with open('test_report.html', 'wb') as file:
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=file, verbosity=2,title='测试报告',description='haha')
    runner.run(suite)
