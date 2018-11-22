# @Time    :2018/11/14 22:12
# @Author  :lvjunjie

import requests
from common.api import request, response, make_session
from utils.cfg import CONFIG
from apis.hbh_dmp_login_api import LoginApi
import re

session_sso = requests.Session()

class User(object):
    def __init__(self):
        self.base_url = CONFIG.BOPSHUNBOHUI_BASE_URL
        self.session = make_session()
        self.headers = {
            'User-Agent': CONFIG.ACCOUNT.User_Agent
        }

    def login_dmp(self, username, password):
        dmp_login = LoginApi()
        res = dmp_login.logindmp(username=username, password=password)
        CASTGC = re.search("CASTGC=(.+?);", res[2].headers['Set-Cookie']).group(1)
        self.ticket = res[1].request.url[40:]
        self.Cookie = res[0].request.headers['Cookie']
        self.Cookie = self.Cookie + "; PHPSESSID=" + self.ticket + "; CASTGC=" + CASTGC
        self.headers['Cookie'] = self.Cookie
        self.SESSION = re.search("SESSION=(.+?);", self.Cookie).group(1)

    @request(url='/iuser/reg/_add', method='post')
    def fast_register(self, phone, user_city_id):
        data = {
            "phone": phone,
            "user_city_id": user_city_id,
            "is_last_six": "on"
        }
        res = self.session.post(url=self.base_url + '/iuser/reg/_add', data=data, headers=self.headers, allow_redirects=False)
        res = self.session.get(res.headers['Location'], allow_redirects=False, headers=self.headers)
        JSESSIONID = re.search("JSESSIONID=(.+?);", res.headers['Set-Cookie']).group(1)
        self.Cookie = self.Cookie + "; PHPSESSID=" + JSESSIONID
        self.headers["Cookie"] = self.Cookie
        res = self.session.get(res.headers['Location'], allow_redirects=False, headers=self.headers)
        ticket = re.search("ticket=(.+)",res.request.url).group(1)
        self.Cookie = "OUTFOX_SEARCH_USER_ID_NCOO=2139139465.580413; jid=d304bdf3e030812ec7065c67e1f785df; SESSION=" + \
                      self.SESSION + "; PHPSESSID=" + ticket.replace(".",'')
        self.headers["Cookie"] = self.Cookie

        return {"data": data, "headers": self.headers}




if __name__ == '__main__':
    user = User()
    user.login_dmp('18000000000', '123456')
    res = user.fast_register('17700000030', '330100')
    print(res.json['err'])
    # headers = (res.request.headers)
    # print(res.headers['Location'])
    # res =requests.get(url=res.headers['Location'], headers=headers)
    # print(res.content)
