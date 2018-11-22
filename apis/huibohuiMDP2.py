
from pithy import request, response
from utils.cfg import CONFIG


class hunbohuiMDP(object):
    def __init__(self):
        self.base_url = CONFIG.CRM_BASE_URL_HTTP
    
    @request(url='/v1/module/add', method='post')
    def add(self):
        """
        添加模块
        """
        
        _json = {
            "moduleDesc": "string",
            "moduleId": "string",
            "moduleName": "string",
            "moduleOwner": "string",
            "modulePhone": "string",
            "moduleStatus": 1,
            "uid": 1
        }
        return response(json=_json)
    
    @request(url='/v1/module/del', method='post')
    def del(self):
        """
        删除模块
        """
        
        params = {
            "moduleId": "string"
        }
        return response(params=params)
    
    @request(url='/v1/module/query', method='post')
    def query(self):
        """
        查询模块
        """
        
        params = {
            "moduleId": "string"
        }
        return response(params=params)
    
    @request(url='/v1/module/update', method='post')
    def update(self):
        """
        修改模块
        """
        
        _json = {
            "moduleDesc": "string",
            "moduleId": "string",
            "moduleName": "string",
            "moduleOwner": "string",
            "modulePhone": "string",
            "moduleStatus": 1,
            "uid": 1
        }
        return response(json=_json)
    
    @request(url='/v1/simple/excute', method='get')
    def excute(self):
        """
        测试
        """
        
        return response()
    
    @request(url='/v1/sms/account/add', method='post')
    def add(self):
        """
        添加短信供应商子账号
        """
        
        _json = {
            "account": "string",
            "password": "string",
            "smsProperties": [
                {
                    "attributeCName": "string",
                    "attributeDesc": "string",
                    "attributeInfo": "string",
                    "attributeName": "string",
                    "attributeQuantization": 1,
                    "attributeValue": "string",
                    "uid": 1
                }
            ],
            "spName": "string",
            "status": 1,
            "type": 1,
            "uid": 1
        }
        return response(json=_json)
    
    @request(url='/v1/sms/account/addCfg', method='post')
    def add_cfg(self):
        """
        添加子账号商配置
        """
        
        params = {
            "owner": "string"
        }
        _json = {
            "attributeCName": "string",
            "attributeDesc": "string",
            "attributeInfo": "string",
            "attributeName": "string",
            "attributeQuantization": 1,
            "attributeValue": "string",
            "uid": 1
        }
        return response(params=params, json=_json)
    
    @request(url='/v1/sms/account/del', method='post')
    def del(self):
        """
        删除子账号
        """
        
        params = {
            "owner": "string"
        }
        return response(params=params)
    
    @request(url='/v1/sms/account/delCfg', method='post')
    def del_cfg(self):
        """
        删除子账号配置
        """
        
        params = {
            "attributeName": "string",
            "owner": "string"
        }
        return response(params=params)
    
    @request(url='/v1/sms/account/query', method='post')
    def query(self):
        """
        查询子账号列表
        """
        
        params = {
            "spEName": "string",
            "status": 1,
            "type": 1
        }
        return response(params=params)
    
    @request(url='/v1/sms/account/queryByName', method='post')
    def query_by_name(self):
        """
        根据子账号查询短信供应商子账号
        """
        
        params = {
            "account": "string"
        }
        return response(params=params)
    
    @request(url='/v1/sms/account/state', method='post')
    def state(self):
        """
        查询短信账号异常履历
        """
        
        params = {
            "owner": "string",
            "spName": "string"
        }
        return response(params=params)
    
    @request(url='/v1/sms/account/status', method='post')
    def status(self):
        """
        短信子账号状态控制
        """
        
        params = {
            "account": "string",
            "status": 1
        }
        return response(params=params)
    
    @request(url='/v1/sms/account/update', method='post')
    def update(self):
        """
        修改子账号配置
        """
        
        _json = {
            "account": "string",
            "password": "string",
            "spName": "string",
            "status": 1,
            "type": 1,
            "uid": 1
        }
        return response(json=_json)
    
    @request(url='/v1/sms/emergency/add', method='post')
    def add(self):
        """
        添加应急短信账号
        """
        
        _json = [
            {
                "account": "string",
                "smsType": 1,
                "uid": 1
            }
        ]
        return response(json=_json)
    
    @request(url='/v1/sms/emergency/del', method='post')
    def del(self):
        """
        删除应急账号
        """
        
        _json = [
            {
                "account": "string",
                "smsType": 1,
                "uid": 1
            }
        ]
        return response(json=_json)
    
    @request(url='/v1/sms/emergency/query', method='post')
    def query(self):
        """
        查询所有应急短信账号
        """
        
        return response()
    
    @request(url='/v1/sms/failed/add', method='post')
    def add(self):
        """
        添加失败策略
        """
        
        _json = [
            {
                "account": "string",
                "failedCount": 1,
                "id": 1,
                "spName": "string",
                "timeInterval": 1,
                "uid": 1
            }
        ]
        return response(json=_json)
    
    @request(url='/v1/sms/failed/del', method='post')
    def del(self):
        """
        删除失败策略
        """
        
        params = {
            "id": 1,
            "uid": 1
        }
        return response(params=params)
    
    @request(url='/v1/sms/failed/query', method='post')
    def query(self):
        """
        查询失败策略
        """
        
        params = {
            "account": "string",
            "id": 1
        }
        return response(params=params)
    
    @request(url='/v1/sms/failed/update', method='post')
    def update(self):
        """
        修改失败策略
        """
        
        _json = [
            {
                "account": "string",
                "failedCount": 1,
                "id": 1,
                "spName": "string",
                "timeInterval": 1,
                "uid": 1
            }
        ]
        return response(json=_json)
    
    @request(url='/v1/sms/history/account', method='post')
    def account(self):
        """
        按账号查询发送量
        """
        
        _json = [
            {
                "minute": "string",
                "property": "string"
            }
        ]
        return response(json=_json)
    
    @request(url='/v1/sms/history/city', method='post')
    def city(self):
        """
        按城市查询发送量
        """
        
        _json = [
            {
                "minute": "string",
                "property": "string"
            }
        ]
        return response(json=_json)
    
    @request(url='/v1/sms/history/day', method='post')
    def day(self):
        """
        按天查询发送量
        """
        
        _json = [
            1
        ]
        return response(json=_json)
    
    @request(url='/v1/sms/history/exhibition', method='post')
    def exhibition(self):
        """
        按展会查询发送量
        """
        
        _json = [
            {
                "minute": "string",
                "property": "string"
            }
        ]
        return response(json=_json)
    
    @request(url='/v1/sms/history/minute', method='post')
    def minute(self):
        """
        按秒查询发送量
        """
        
        _json = [
            "string"
        ]
        return response(json=_json)
    
    @request(url='/v1/sms/history/moduleId', method='post')
    def module_id(self):
        """
        按模块查询发送量
        """
        
        _json = [
            {
                "minute": "string",
                "property": "string"
            }
        ]
        return response(json=_json)
    
    @request(url='/v1/sms/history/query', method='post')
    def query(self):
        """
        按条件查询
        """
        
        params = {
            "city": "string",
            "cursor": 1,
            "exhibition": "string",
            "month": 1,
            "phone": "string",
            "size": 1,
            "type": 1,
            "year": 1
        }
        return response(params=params)
    
    @request(url='/v1/sms/history/queryById', method='post')
    def query_by_id(self):
        """
        按主键查单条
        """
        
        params = {
            "id": 1,
            "month": 1,
            "year": 1
        }
        return response(params=params)
    
    @request(url='/v1/sms/history/spName', method='post')
    def sp_name(self):
        """
        按短信供应商查询发送量
        """
        
        _json = [
            {
                "minute": "string",
                "property": "string"
            }
        ]
        return response(json=_json)
    
    @request(url='/v1/sms/history/taskId', method='post')
    def task_id(self):
        """
        按任务号查询发送量
        """
        
        _json = {}
        return response(json=_json)
    
    @request(url='/v1/sms/history/templateId', method='post')
    def template_id(self):
        """
        按模板查询发送量
        """
        
        _json = {}
        return response(json=_json)
    
    @request(url='/v1/sms/history/type', method='post')
    def type(self):
        """
        按短信类型查询发送量
        """
        
        _json = {}
        return response(json=_json)
    
    @request(url='/v1/sms/priority/add', method='post')
    def add(self):
        """
        添加路由规则
        """
        
        _json = {}
        return response(json=_json)
    
    @request(url='/v1/sms/priority/del', method='post')
    def del(self):
        """
        删除路由规则
        """
        
        params = {
            "id": 1
        }
        return response(params=params)
    
    @request(url='/v1/sms/priority/query', method='post')
    def query(self):
        """
        查询路由规则
        """
        
        params = {
            "city": "string",
            "exhibition": "string",
            "type": 1
        }
        return response(params=params)
    
    @request(url='/v1/sms/priority/update', method='post')
    def update(self):
        """
        修改路由规则
        """
        
        _json = {}
        return response(json=_json)
    
    @request(url='/v1/sms/send/smsMessagesBatchReq', method='post')
    def sms_messages_batch_req(self):
        """
        相同内容短信发送参数对象(按模板发送)
        """
        
        _json = {}
        return response(json=_json)
    
    @request(url='/v1/sms/send/smsMessagesBatchTextReq', method='post')
    def sms_messages_batch_text_req(self):
        """
        相同内容短信发送参数对象(文本发送)
        """
        
        _json = {}
        return response(json=_json)
    
    @request(url='/v1/sms/send/smsMessagesReq', method='post')
    def sms_messages_req(self):
        """
        不同内容短信发送参数对象(按模板发送)
        """
        
        _json = {}
        return response(json=_json)
    
    @request(url='/v1/sms/send/smsMessagesTextReq', method='post')
    def sms_messages_text_req(self):
        """
        个性化内容短信发送参数对象(文本发送)
        """
        
        _json = {}
        return response(json=_json)
    
    @request(url='/v1/sms/send/timing/smsMessagesBatchReq', method='post')
    def sms_messages_batch_req(self):
        """
        相同内容短信发送参数对象(按模板发送)
        """
        
        params = {
            "time": "string"
        }
        _json = {}
        return response(params=params, json=_json)
    
    @request(url='/v1/sms/send/timing/smsMessagesBatchTextReq', method='post')
    def sms_messages_batch_text_req(self):
        """
        相同内容短信发送参数对象(文本发送)
        """
        
        params = {
            "time": "string"
        }
        _json = {}
        return response(params=params, json=_json)
    
    @request(url='/v1/sms/send/timing/smsMessagesReq', method='post')
    def sms_messages_req(self):
        """
        不同内容短信发送参数对象(按模板发送)
        """
        
        params = {
            "time": "string"
        }
        _json = {}
        return response(params=params, json=_json)
    
    @request(url='/v1/sms/send/timing/smsMessagesTextReq', method='post')
    def sms_messages_text_req(self):
        """
        个性化内容短信发送参数对象(文本发送)
        """
        
        params = {
            "time": "string"
        }
        _json = {}
        return response(params=params, json=_json)
    
    @request(url='/v1/sms/sp/add', method='post')
    def add(self):
        """
        添加短信供应商
        """
        
        _json = {}
        return response(json=_json)
    
    @request(url='/v1/sms/sp/addCfg', method='post')
    def add_cfg(self):
        """
        添加供应商配置
        """
        
        params = {
            "owner": "string"
        }
        _json = {}
        return response(params=params, json=_json)
    
    @request(url='/v1/sms/sp/del', method='post')
    def del(self):
        """
        删除供应商
        """
        
        params = {
            "owner": "string"
        }
        return response(params=params)
    
    @request(url='/v1/sms/sp/delCfg', method='post')
    def del_cfg(self):
        """
        删除供应商配置
        """
        
        params = {
            "attributeName": "string",
            "owner": "string"
        }
        return response(params=params)
    
    @request(url='/v1/sms/sp/query', method='post')
    def query(self):
        """
        查询短信供应商列表
        """
        
        return response()
    
    @request(url='/v1/sms/sp/queryByName', method='post')
    def query_by_name(self):
        """
        根据名称查询短信供应商
        """
        
        params = {
            "spEName": "string"
        }
        return response(params=params)
    
    @request(url='/v1/sms/sp/update', method='post')
    def update(self):
        """
        修改供应商配置
        """
        
        _json = {}
        return response(json=_json)
    
    @request(url='/v1/sms/task/cancel', method='post')
    def cancel(self):
        """
        取消发送
        """
        
        params = {
            "id": 1,
            "uid": 1
        }
        return response(params=params)
    
    @request(url='/v1/sms/task/create', method='post')
    def create(self):
        """
        创建短信发送任务
        """
        
        _json = {}
        return response(json=_json)
    
    @request(url='/v1/sms/task/del', method='post')
    def del(self):
        """
        删除短信发送任务
        """
        
        params = {
            "id": 1,
            "uid": 1
        }
        return response(params=params)
    
    @request(url='/v1/sms/task/query', method='post')
    def query(self):
        """
        查询短信发送任务
        """
        
        params = {
            "length": 1,
            "start": 1,
            "taskInfo": "string",
            "title": "string"
        }
        return response(params=params)
    
    @request(url='/v1/sms/task/send', method='post')
    def send(self):
        """
        执行发送
        """
        
        params = {
            "id": 1,
            "uid": 1
        }
        return response(params=params)
    
    @request(url='/v1/sms/template/add', method='post')
    def add(self):
        """
        添加模板
        """
        
        _json = {}
        return response(json=_json)
    
    @request(url='/v1/sms/template/del', method='post')
    def del(self):
        """
        删除模板
        """
        
        params = {
            "id": 1,
            "key": "string",
            "uid": 1
        }
        return response(params=params)
    
    @request(url='/v1/sms/template/query', method='post')
    def query(self):
        """
        查询模板
        """
        
        params = {
            "key": "string",
            "name": "string",
            "sendTemplateClassify": 1
        }
        return response(params=params)
    
    @request(url='/v1/sms/template/update', method='post')
    def update(self):
        """
        修改模板
        """
        
        _json = {}
        return response(json=_json)
    
    @request(url='/v1/sms/whiteList/add', method='post')
    def add(self):
        """
        添加白名单
        """
        
        params = {
            "moduleId": "string",
            "phones": "string",
            "uid": 1
        }
        return response(params=params)
    
    @request(url='/v1/sms/whiteList/del', method='post')
    def del(self):
        """
        删除白名单
        """
        
        params = {
            "moduleId": "string",
            "phones": "string"
        }
        return response(params=params)
    
    @request(url='/v1/sms/whiteList/query', method='post')
    def query(self):
        """
        查询白名单
        """
        
        params = {
            "moduleId": "string"
        }
        return response(params=params)
    