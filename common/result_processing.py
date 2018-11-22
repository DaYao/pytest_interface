import requests

# {time}秒能失败{failed_count}次，发起告警，
# 失败后发送邮件给{receivers},邮件主题为{subject}，内容为失败具体原因

host = 'http://lvjunjie.cn:5002'
# host = 'http://localhost:5000'
product_id = 1
failed_count = 999
time = 600
receivers = ['lvjunjie84@hotmail.com']
subject = '业务失败告警'


class ResultProcessing:
    def __init__(self):
        self.base_url = host
        self.header = {
            'Content-Type': 'application/json'
        }


    def result_processing(self, assert_content, tc_name, failed_content=None):
        if assert_content == 'passed':
            """通过情况"""
            query = '/monitor/passresult'
            headers = self.header
            json = {
                'product_id': product_id,
                'tc_name': tc_name
            }
            res = requests.post(url=self.base_url + query, headers=headers, json=json,
                                allow_redirects=False)
            res_json = res.json()
            return res_json['msg']

        elif assert_content == "failed":
            """失败情况"""
            query = '/monitor/failresult'
            headers = self.header
            json = {
                'product_id': product_id,
                'tc_name': tc_name,
                'failed_content': failed_content

            }
            res = requests.post(url=self.base_url + query, headers=headers, json=json,
                                allow_redirects=False)
            res_json = res.json()
            return res_json['msg']
        else:
            pass


class Alarm:
    def __init__(self):
        self.base_url = host
        self.header = {
            'Content-Type': 'application/json'
        }

    def service_alarm_email(self, message):
        query = '/monitor/alarm'
        headers = self.header
        json = {
            "product_id": product_id,
            "alarm_level": 1,
            "failed_count": failed_count,
            "time": time,
            "data": {
                "receivers": receivers,
                "subject": subject,
                "message": message
            }
        }
        res = requests.post(url=self.base_url + query, headers=headers, json=json,
                            allow_redirects=False)
        res_json = res.json()
        return res_json['msg']

    def service_alarm_dingding(self, content=None, to_login_names=[]):
        json = {
            "channel": "ding",
            "channel_args": {
                "msgtype": "text",
                "msgbody": {
                    "content": content
                }
            },
            "to_login_names": to_login_names
        }
        return requests.post(url="http://172.16.210.13:5202/send_message", json=json)


if __name__ == '__main__':
    a = Alarm()
    print(a.service_alarm_dingding("test2", ["lvjunjie"]))