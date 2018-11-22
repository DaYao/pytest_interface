from pithy import request, response
from utils.cfg import CONFIG


class HbhMdpAccount(object):
    def __init__(self):
        self.base_url = CONFIG.MDP_BASE_URL

    @request(url='/v1/sms/account/add', method='post')
    def account_add(self, account=None, password=None, smsProperties=[], spName=None, status=0, type=0, uid=0):
        """
        添加短信供应商子账号
        """
        _json = {
            "account": account,
            "password": password,
            "smsProperties": smsProperties,

            #      [
            #     {
            #         "attributeCName": "string",
            #         "attributeDesc": "string",
            #         "attributeInfo": "string",
            #         "attributeName": "string",
            #         "attributeQuantization": 1,
            #         "attributeValue": "string",
            #         "uid": 1
            #     }
            # ],
            "spName": spName,
            "status": status,
            "type": type,
            "uid": uid
        }
        return response(json=_json)


    @request(url='/v1/sms/account/addCfg', method='post')
    def account_add_cfg(self,owner=None, uid=None, attributeCName=None, attributeDesc=None, attributeInfo=None,
                        attributeName=None, attributeQuantization=None, attributeValue=None ):
        """
        添加子账号商配置
        """

        params = {
            "owner": owner
        }
        _json = {
            "attributeCName":attributeCName,
            "attributeDesc": attributeDesc,
            "attributeInfo": attributeInfo,
            "attributeName": attributeName,
            "attributeQuantization": attributeQuantization,
            "attributeValue": attributeValue,
            "uid": uid
        }
        return response(params=params, json=_json)

    @request(url='/v1/sms/account/del', method='post')
    def account_del(self, owner):
        """
        删除子账号
        """

        params = {
            "owner": owner
        }
        return response(params=params)

    @request(url='/v1/sms/account/delCfg', method='post')
    def account_del_cfg(self, attributeName=None, owner=None ):
        """
        删除子账号配置
        """

        params = {
            "attributeName":attributeName,
            "owner": owner
        }
        return response(params=params)

    @request(url='/v1/sms/account/query', method='post')
    def account_query(self,spEName=None, status=0, type=0):
        """
        查询子账号列表
        """

        params = {
            "spEName": spEName,
            "status": status,
            "type": type
        }
        return response(params=params)

    @request(url='/v1/sms/account/queryByName', method='post')
    def account_query_by_name(self, account):
        """
        根据子账号查询短信供应商子账号
        """

        params = {
            "account": account
        }
        return response(params=params)

    @request(url='/v1/sms/account/state', method='post')
    def account_state(self, owner=None, spName=None):
        """
        查询短信账号异常履历
        """

        params = {
            "owner": owner,
            "spName": spName
        }
        return response(params=params)

    @request(url='/v1/sms/account/status', method='post')
    def account_status(self,account=None, status=0):
        """
        短信子账号状态控制
        """

        params = {
            "account": account,
            "status": status
        }
        return response(params=params)

    @request(url='/v1/sms/account/update', method='post')
    def account_update(self,account=None, password=None, spName=None, status=0, type=0, uid=0):
        """
        修改子账号配置
        """

        _json = {
            "account": account,
            "password": password,
            "spName": spName,
            "status": status,
            "type": type,
            "uid": uid
        }
        return response(json=_json)


class HbhMdpSmsMessage:
    def __init__(self):
        self.base_url = CONFIG.MDP_BASE_URL

    @request(url='/v1/sms/send/smsMessagesBatchReq', method='post')
    def sms_messages_batch_req(self):
        """
        相同内容短信发送参数对象(按模板发送)
        """

        _json = {
              "buid": "SDG147852",
              "city": "北京",
              "exhibition": "家芭莎",
              "isOpenWhitelist": True,
              "moduleId": "DMPCRM01",
              "parameters": {},
              "planTime": "2018-10-31 11:34:00",
              "receiverPhones": [
                "string"
              ],
              "smsType": 1,
              "spare1": "您当前城市、活动、类型下的只有1条短信通道，低于3条，请联系MDP处理",
              "taskId": "MK20181031001",
              "templateId": "jiehun_dmp_test_01"
        }
        return response(json=_json)

    @request(url='/v1/sms/send/smsMessagesBatchTextReq', method='post')
    def sms_messages_batch_text_req(self):
        """
        相同内容短信发送参数对象(文本发送)
        """

        _json = {
              "buid": "SDG147852",
              "city": "北京",
              "exhibition": "家芭莎",
              "isOpenWhitelist": True,
              "moduleId": "DMPCRM01",
              "planTime": "2018-10-31 11:34:00",
              "receiverPhones": [
                "string"
              ],
              "smsContent": "亲爱的，您通过报名参加婴芭莎·童尚大典的上传资料已审核通过，请登录婴芭莎APP，点击童尚大典，进入我的个人主页查看。并请持续关注APP童尚大典复赛消息、结果及赛事进程。",
              "smsType": 1,
              "spare1": "您当前城市、活动、类型下的只有1条短信通道，低于3条，请联系MDP处理",
              "taskId": "MK147852"
        }
        return response(json=_json)

    @request(url='/v1/sms/send/smsMessagesReq', method='post')
    def sms_messages_req(self):
        """
        不同内容短信发送参数对象(按模板发送)
        """

        _json = {
              "buid": "SDG147852",
              "city": "北京",
              "exhibition": "家芭莎",
              "isOpenWhitelist": True,
              "moduleId": "DMPCRM01",
              "phones": [
                {
                  "parameters": "${v_code}=147852",
                  "phone": 15157181386,
                  "templateId": "jiehun_dmp_test_01"
                }
              ],
              "planTime": "2018-10-31 11:34:00",
              "smsType": 1,
              "spare1": "您当前城市、活动、类型下的只有1条短信通道，低于3条，请联系MDP处理"
         }
        return response(json=_json)

    @request(url='/v1/sms/send/smsMessagesTextReq', method='post')
    def sms_messages_text_req(self):
        """
        个性化内容短信发送参数对象(文本发送)
        """

        _json = {
              "buid": "SDG147852",
              "city": "北京",
              "exhibition": "家芭莎",
              "isOpenWhitelist": True,
              "moduleId": "DMPCRM01",
              "phones": [
                {
                  "msg": "亲爱的，您通过报名参加婴芭莎·童尚大典的上传资料已审核通过，请登录婴芭莎APP，点击童尚大典，进入我的个人主页查看。并请持续关注APP童尚大典复赛消息、结果及赛事进程。",
                  "phone": 15157181386
                }
              ],
              "planTime": "2018-10-31 11:34:00",
              "smsType": 1,
              "spare1": "您当前城市、活动、类型下的只有1条短信通道，低于3条，请联系MDP处理"
        }
        return response(json=_json)

    @request(url='/v1/sms/send/timing/smsMessagesBatchReq', method='post')
    def sms_messages_batch_req(self):
        """
        相同内容短信发送参数对象(按模板发送)
        """
        _json = {
              "buid": "SDG147852",
              "city": "北京",
              "exhibition": "家芭莎",
              "isOpenWhitelist": True,
              "moduleId": "DMPCRM01",
              "parameters": {},
              "planTime": "2018-10-31 11:34:00",
              "receiverPhones": [
                "string"
              ],
              "smsType": 1,
              "spare1": "您当前城市、活动、类型下的只有1条短信通道，低于3条，请联系MDP处理",
              "taskId": "MK20181031001",
              "templateId": "jiehun_dmp_test_01"
        }
        params = {
            "time": "string"
        }

        return response(params=params, json=_json)

    @request(url='/v1/sms/send/timing/smsMessagesBatchTextReq', method='post')
    def sms_messages_batch_text_req(self):
        """
        相同内容短信发送参数对象(文本发送)
        """

        params = {
            "time": "string"
        }
        _json = {
              "buid": "SDG147852",
              "city": "北京",
              "exhibition": "家芭莎",
              "isOpenWhitelist": True,
              "moduleId": "DMPCRM01",
              "planTime": "2018-10-31 11:34:00",
              "receiverPhones": [
                "string"
              ],
              "smsContent": "亲爱的，您通过报名参加婴芭莎·童尚大典的上传资料已审核通过，请登录婴芭莎APP，点击童尚大典，进入我的个人主页查看。并请持续关注APP童尚大典复赛消息、结果及赛事进程。",
              "smsType": 1,
              "spare1": "您当前城市、活动、类型下的只有1条短信通道，低于3条，请联系MDP处理",
              "taskId": "MK147852"
        }
        return response(params=params, json=_json)

    @request(url='/v1/sms/send/timing/smsMessagesReq', method='post')
    def sms_messages_req(self):
        """
        不同内容短信发送参数对象(按模板发送)
        """

        params = {
            "time": "string"
        }
        _json = {
              "buid": "SDG147852",
              "city": "北京",
              "exhibition": "家芭莎",
              "isOpenWhitelist": True,
              "moduleId": "DMPCRM01",
              "phones": [
                {
                  "parameters": "${v_code}=147852",
                  "phone": 15157181386,
                  "templateId": "jiehun_dmp_test_01"
                }
              ],
              "planTime": "2018-10-31 11:34:00",
              "smsType": 1,
              "spare1": "您当前城市、活动、类型下的只有1条短信通道，低于3条，请联系MDP处理"
        }
        return response(params=params, json=_json)

    @request(url='/v1/sms/send/timing/smsMessagesTextReq', method='post')
    def sms_messages_text_req(self):
        """
        个性化内容短信发送参数对象(文本发送)
        """

        params = {
            "time": "string"
        }
        _json = {
              "buid": "SDG147852",
              "city": "北京",
              "exhibition": "家芭莎",
              "isOpenWhitelist": True,
              "moduleId": "DMPCRM01",
              "phones": [
                {
                  "msg": "亲爱的，您通过报名参加婴芭莎·童尚大典的上传资料已审核通过，请登录婴芭莎APP，点击童尚大典，进入我的个人主页查看。并请持续关注APP童尚大典复赛消息、结果及赛事进程。",
                  "phone": 15157181386
                }
              ],
              "planTime": "2018-10-31 11:34:00",
              "smsType": 1,
              "spare1": "您当前城市、活动、类型下的只有1条短信通道，低于3条，请联系MDP处理"
        }
        return response(params=params, json=_json)


if __name__ == '__main__':
    hbh_dmp = HbhMdpSmsMessage()
    res = hbh_dmp.sms_messages_batch_req()
    print(res.content)