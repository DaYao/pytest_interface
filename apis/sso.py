# coding=utf-8
import re
from pithy import request, response, make_session
from common.utils import get_md5
from utils.cfg import CONFIG


class SSO(object):
    def __init__(self):
        self.base_url = CONFIG.SSOHUNBOHUI_BASE_URL
        self.session = make_session

    @request(url='/login', method='get')
    def _get_cookie(self):
        return response()


    @request(method='post')
    def sso_login(self, login_name, password):
        """
        后台sso统一认证
        """
        res = self._get_cookie()
        res.encoding = 'utf-8'
        url = re.search("action=\"(.+?)\"", res.text).group(1)
        lt = re.search("name=\"lt\"\s+value=\"(.+?)\"", res.text).group(1)
        execution = re.search("name=\"execution\"\s+value=\"(.+?)\"", res.text).group(1)
        _eventId = re.search("name=\"_eventId\"\s+value=\"(.+?)\"", res.text).group(1)
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        }
        # vcode  验证码，测试环境随便
        params = {"username": login_name,
                  "password": get_md5(password),
                  "vcode": '111111',
                  'lt': lt,
                  'execution': execution,
                  '_eventId': _eventId,
                  "submit": '登录'}
        return response(url=url, data=params, headers=headers)


if __name__ == '__main__':
    a = SSO()
    m = a.sso_login(*CONFIG.ACCOUNT.APP_USER).content
