# coding=utf-8
from common.api import request,response
from utils.cfg import CONFIG
import requests


class DmpBopsApi(object):
    def __init__(self):
        self.base_url = CONFIG.BOPSHUNBOHUI_BASE_URL

    @request(url='store/list', method='get')
    def store_list(self, cookie):
            """
            商城---店铺管理---店铺列表
            """
            data = {
            }
            headers = {
                "Host": 'bops.test.tthunbohui.com',
                "Upgrade-Insecure-Requests": '1',
                "Content-Type": 'application/x-www-form-urlencoded',
                "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
                "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                "Referer": 'http://bops.test.tthunbohui.com/',
                "Accept-Encoding": 'gzip, deflate',
                "Accept-Language": 'zh-CN,zh;q=0.9',
                "Cookie": cookie,
                "Connection": 'keep-alive',
            }
            return response(data=data, headers=headers)

