from class_super.http_request import HttpRequest


class PythonHttpRequest(HttpRequest):
    def __init__(self, method, url, data):  # 与父类同名方法，为重写
        self.method = method
        super(HttpRequest).__init__(url, data)   # 超继承，继承父类的url，data

    def print_msg(self):
        print('我是无用函数，我要调用父类函数')
        if self.method == 'get':
            self.get_requests()
        elif self.method == 'post':
            self.post_requests()


