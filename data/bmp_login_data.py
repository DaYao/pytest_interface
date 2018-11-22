# @Time    :2018/10/29 17:29
# @Author  :lvjunjie 
from utils.cfg import CONFIG


class DmpLoginCase:
    def dmp_login_data(self):
        return [
            {
                "username": CONFIG.ACCOUNT.CRM_USER[0],
                "password": CONFIG.ACCOUNT.CRM_USER[1],
                "assert_contents": ["设置", "商城", "社区", "活动", "内容", "营销", "用户", "积分", "婚博会", "APP", "答题",
                                    "攻略", "搜索", "任务体系", "结婚小工具"],
                "assert_contents_not": ["密码错误"]
            },
            {
                "username": CONFIG.ACCOUNT.APP_USER[0],
                "password": CONFIG.ACCOUNT.APP_USER[1],
                "assert_contents": ["设置", "商城", "社区", "活动", "内容", "营销", "用户", "积分", "婚博会", "APP", "答题",
                                    "攻略", "搜索", "任务体系", "结婚小工具"],
                "assert_contents_not": ["密码错误"]
            },
            {
                "username": CONFIG.ACCOUNT.APP_USER[0],
                "password": '1234567890',
                "assert_contents_not":["设置", "商城", "社区", "活动", "内容", "营销", "用户", "积分", "婚博会", "APP", "答题",
                                    "攻略", "搜索", "任务体系", "结婚小工具"],
                "assert_contents": ["密码错误"]
            }
        ]

