# @Time    :2018/11/12 20:27
# @Author  :lvjunjie
from apis.huibohui_MDP_api import HBHMDP



class TestAccount:

    def test_account(self):

        hbh_mdp = HBHMDP()
        res = hbh_mdp.account_add(account='test_ljj', password='123456', smsProperties=[], spName='test短信商',
                                  status=1, type=1, uid=2596717951348375600)
        res_json = res.json

        res = hbh_mdp.account_add_cfg(owner='test_ljj1', uid=2596717951348375600)
        res_json = res.json

