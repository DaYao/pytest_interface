# @Time    :2018/12/3 15:27
# @Author  :lvjunjie

import json
import re
import yaml
import urllib.parse
import os
from jinja2 import Template


def list_to_input(list=[]):
    input = ""
    for i in list:
        input = input + '        "{}": {},\n'.format(str(i),str(i))
    input = "{\n" + input[:-2] + "\n    }"
    return input


class ProxyToPytest(object):
    def __init__(self, file_path):
        # with open(file_path, "r") as f:
        #     self.strline = f.readlines()  # 读取文件内容
        #     print(self.strline)
        print(file_path)
        self.strline = file_path.split('\n')
        # print(self.strline)

    def __get_method(self):
        self.method = re.search("^(.+?) ", self.strline[0]).group(1).lower()
        return self.method

    def get_method(self):
        self.method = re.search("^(.+?) ", self.strline[0]).group(1).lower()
        return self.method


    def get_url(self):
        self.url = ''
        if '?' in self.strline[0]:
            url = re.search("^(.+?) (.+?)\?.+", self.strline[0]).group(2)
        else:
            url = re.search("^(.+?) (.+?) ", self.strline[0]).group(2)
        self.url = url
        return self.url

    def get_params(self):
        self.params = ''
        if '?' in self.strline[0]:
            params_from = re.search("\?(.+?) ", self.strline[0]).group(1)
            params_k, params_v = [], []
            params = ''
            params_from_list = params_from.split('&')
            for i in params_from_list:
                params_k.append(i.split('=', 1)[0])
                params_v.append(i.split('=', 1)[1])
            for j in range(len(params_k)):
                params = params + '    "{}": "{}",\n'.format(params_k[j], params_v[j])
            params = params[:-2]
            self.params = yaml.load("{\n" + params + "\n }")
            return ("params = {\n" + params + "\n}", list(self.params.keys()))
        else:
            return self.params, []

    def get_headers(self):
        headers_k,headers_v = [], []
        for i in range(1, len(self.strline)-1):
            try:
                # 过滤headers部分字段
                if self.strline[i].split(':', 1)[0] in ["Connection", "Accept-Encoding", "Accept", "Content-Length"]:
                    continue
                headers_k.append(self.strline[i].split(':',1)[0].replace(" ",""))
                headers_v.append(self.strline[i].split(':',1)[1].split('\n',1)[0].replace(" ",""))
            except:
                pass
        headers = ""
        for j in range(0, len(headers_k) - 1):
            headers = headers + '        "{}": "{}",\n'.format(headers_k[j], headers_v[j])
        self.headers = yaml.load("{\n" + headers + "\n }")
        return ("headers = {\n" + headers + "    }")

    def __get_headers(self):
        headers_k, headers_v = [], []
        for i in range(1, len(self.strline)-1):
            try:
                # 过滤headers部分字段
                if self.strline[i].split(':', 1)[0] in ["Connection", "Accept-Encoding", "Accept", "Content-Length"]:
                    continue
                headers_k.append(self.strline[i].split(':', 1)[0])
                headers_v.append(self.strline[i].split(':', 1)[1].split('\n',1)[0])
            except:
                pass
        headers = ""
        for j in range(0, len(headers_k) - 1):
            headers = headers + '"{}": "{}",\n'.format(headers_k[j], headers_v[j])
        self.headers = yaml.load("{\n" + headers + "\n}")
        return (self.headers)

    def get_body(self):
        self.data = {}
        self.json = {}
        method = self.__get_method()
        headers = self.__get_headers()
        body = self.strline[-1]
        # urldecode
        body = urllib.parse.unquote(body)
        if method == 'post':
            if "x-www-form-urlencoded" in headers["Content-Type"]:
                # print("body = ", body)
                body_k, body_v = [], []
                data = ''
                body_list = body.split('&')
                self.data_str = ""
                if body_list[0]:
                    for i in body_list:
                        body_k.append(i.split('=', 1)[0])
                        body_v.append(i.split('=', 1)[1])
                    for j in range(len(body_k)):
                        data = data + '"{}": "{}",\n'.format(body_k[j], body_v[j])
                    self.data = yaml.load("{\n" + data[:-2] + "\n}")
                    self.data_str = urllib.parse.unquote(json.dumps(self.data, indent=4))
                return ("data = " + self.data_str + " \n    }"), body_k
            elif "json" in headers["Content-Type"]:
                self.json = yaml.load(body)
                self.json_str = urllib.parse.unquote(json.dumps(self.json, indent=4))
                return "json = " + self.json_str, list(self.json.keys())
        else:
            return '', []


if __name__ == '__main__':
    str_path = """GET /taskengine/task/list?filterTaskId=&page=1&size=20 HTTP/1.1
Host: bops.test.tthunbohui.com
Accept: */*
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36
Referer: http://bops.test.tthunbohui.com/taskengine/task/list-page
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: jid=6f1d38c68b84cf788c031ed49334ae56; ciid=0; PHPSESSID=ST-2393-De3sNSSOpfL5vfuIFCkb-cas01exampleorg; SESSION=3bc5e6ec-27af-4d36-b944-b457fabec1b6
Connection: keep-alive"""
    proxy_file = os.getenv('proxy_file', str_path)


    proxy_to_pytest = ProxyToPytest(proxy_file)
    method = proxy_to_pytest.get_method()
    headers = proxy_to_pytest.get_headers()
    url = proxy_to_pytest.get_url()
    # print(proxy_to_pytest.headers)
    host = proxy_to_pytest.headers['Host']
    # print('host=', host)

    inter_name = url.replace("/", "_")[1:]
    params = proxy_to_pytest.get_params()[0]
    params_params = proxy_to_pytest.get_params()[1]
    params_params_str = ""
    for i in params_params:
        params_params_str = params_params_str + ", " + i
    # print(params_params_str)
    body = proxy_to_pytest.get_body()[0]
    body_params = proxy_to_pytest.get_body()[1]
    body_params_str = ""
    for i in body_params:
        body_params_str = body_params_str + ", " + i
    # print(body_params_str)
    # print("method = ", method)
    # print(headers)
    # print("url = ", url)
    # print(params)
    # print(body)
    # print(body_params)
    # print(inter_name)
    # print(list_to_input(params_params))
    print("\n")
    print("--------------------您的requests代码--------------------")
    inter_params = ''
    if params:
        inter_params = inter_params + params_params_str
    if body:
        inter_params = inter_params + body_params_str
    # print(inter_params)
    # 生成API
    API = "import requests\n"
    # API = "@request(url='{}', method='{}')\n".format(url, method, body_params_str) + "def {}(self".format(inter_name)
    _return = ""
    # API = API + inter_params + "):\n"
    if headers:
        API = API + headers + "\n"
        _return = _return + '{}={}, '.format("headers", "headers")
    if params:
        API = API + params + "\n"
        _return = _return + '{}={}, '.format("params", "params")
    if body:
        API = API + body + "\n"
        _return = _return + '{}={}, '.format(body[0:4], body[0:4])
    API = API.encode('latin-1').decode('unicode_escape')
    _return = 'requests.{}(url="http://{}", {})'.format(method, host+url, _return[:-2])
    API = API + _return
    print(API)


    print("\n\n\n")
    print("--------------------您的请求数据--------------------")

    # 生成data
    DATA = {}
    if params:
        DATA.update(proxy_to_pytest.params)
    if body:
        if proxy_to_pytest.data:
            DATA.update(proxy_to_pytest.data)
        if proxy_to_pytest.json:
            DATA.update(proxy_to_pytest.json)
    DATA = urllib.parse.unquote(json.dumps(DATA, indent=4))
    DATA = "def " + inter_name + "(self):\n    return [    \n        " + DATA.replace('\n', '\n        ') + '\n    ]'
    DATA = DATA.encode('latin-1').decode('unicode_escape')

    print(DATA)

    print("\n")
    print("--------------------生成CASE--------------------")
    # 生成case
    case_list = []
    CASE = ''
    if params_params:
        case_list = case_list + params_params
    if body_params:
        case_list = case_list + body_params
    for i in case_list:
        CASE = CASE + '{}=data["{}"], '.format(i, i)
    CASE = "res = CLASS.{}({})".format(inter_name, CASE[:-2])
    print(CASE)






