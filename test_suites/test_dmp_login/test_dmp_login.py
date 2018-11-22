from apis.hbh_dmp_login_api import LoginApi
from db.hunbohui_db import get_content_from_phone
from data.bmp_login_data import DmpLoginCase
from utils.cfg import CONFIG
import pytest

dmp_login_data = DmpLoginCase().dmp_login_data()

class TestLogin(object):

    @pytest.mark.parametrize('data', dmp_login_data)
    def test_login_session(self, data):
        """
        登录测试
        """
        dmp = LoginApi()
        res = dmp.logindmp(data['username'], data['password'])
        res_content = res.text
        for assert_text in data["assert_contents"]: assert assert_text in res_content


