import requests
import json

uat_url = 'https://uatleague.round-table-union.com/api/rts/base/home/login/v110'

header = {
    'content-type': 'application/json',
    'version': '1.3.1',
    'platform': 'iOS',
    'deviceId': '287171e242270fb7ce193486b0e61f41'
}

payload = {
    "smsCodeToken": "",
    "standbyUniqueIdentification": "_Android10",
    "deviceUniqueIdentification": "",
    "password": 'e10adc3949ba59abbe56e057f20f883e',
    "loginType": "1",
    "smsCode": "",
    "loginCode": '13011111111',
    "source": "",
    "applicationId": "AoSf3sOaLVENjofVUhIoMRt-Pjs7603WuGNytkwvoC2y"
}

r = requests.post(url=uat_url, headers=header, data=json.dumps(payload), verify=False)
print(r.json())


