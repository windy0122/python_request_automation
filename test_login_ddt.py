import requests
from ddt import ddt, data, unpack
import unittest
from class_unittest.get_data import GetData
import json


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

