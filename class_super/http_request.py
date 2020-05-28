import requests


class HttpRequest:
    def __init__(self, url, data):
        self.url = url
        self.data = data

    def get_requests(self):
        res = requests.get(self.url, self.data)
        print('get请求结果{0}'.format(res))

    def post_requests(self):
        res = requests.post(self.url, self.data)
        print('get请求结果{0}'.format(res))
