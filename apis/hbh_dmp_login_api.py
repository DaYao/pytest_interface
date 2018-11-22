# @Time    :2018/10/29 16:57
# @Author  :lvjunjie
from utils.cfg import CONFIG
import requests
from common import utils
from db.hunbohui_db import get_content_from_phone
import re


class LoginApi(object):

    def logindmp(self, username, password):
        """
        dmp平台账号密码登录
        """
        session_sso = requests.Session()
        cookie = {
            "OUTFOX_SEARCH_USER_ID_NCOO":"2139139465.580413"
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                          "like Gecko) Chrome/70.0.3538.77 Safari/537.36",
            # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            # "Accept-Encoding": 'gzip, deflate',
            # "Accept-Language": 'zh-CN,zh;q=0.9,en;q=0.8',
            # "Upgrade-Insecure-Requests": "1"
        }

        res_sso = session_sso.get(url=CONFIG.BOPSHUNBOHUI_BASE_URL, headers=headers, cookies=cookie)
        test_sso = res_sso.text
        lt = re.search("name=\"lt\" value=\"(.+?)\"", test_sso).group(1)
        Set_Cookie = res_sso.headers["Set-Cookie"]
        JSESSIONID = Set_Cookie[11:43]

        PHONE = username
        sms_content = get_content_from_phone(PHONE)
        vcode = re.findall(u'(验证码:)(\d+).+', sms_content)[0][1]

        params = {
            'service': 'http://bops.test.tthunbohui.com/'
        }
        data = {
            "username": username,
            "password": utils.get_md5(password),
            "vcode": vcode,
            "lt": lt,
            "execution": 'e1s1',
            "_eventId":  'submit',
            "submit": '%E7%99%BB%E5%BD%95'
        }
        headers = {
            "Cache-Control": 'max-age=0',
            # "Origin": 'http://sso.test.tthunbohui.com',
            # "Upgrade-Insecure-Requests": '1',
            "Content-Type": 'application/x-www-form-urlencoded',
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                          'like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            # "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            # "Referer": 'http://sso.test.tthunbohui.com/login?service=http%3A%2F%2Fbops.test.tthunbohui.com%2F',
        }

        res2 = session_sso.post(url=CONFIG.SSOHUNBOHUI_BASE_URL + '/login;jsessionid=' + JSESSIONID, params=params,
                                data=data, headers=headers, cookies=cookie, allow_redirects=False)
        Location = res2.headers['Location']
        # print(res2.headers['Set-Cookie'])
        # print(Location)
        res1 = session_sso.get(url=Location, allow_redirects=False)
        ticket = res1.request.url[40:]
        # print(ticket)
        # Location = res.headers['Location']
        # print(Location)
        res = session_sso.get(url=Location, allow_redirects=False)
        return res, res1, res2
        print(res.request.headers)

        # return response(data=data, params=params, headers=headers)


