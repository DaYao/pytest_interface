from pithy import request, response, make_session
from utils.cfg import CONFIG


class HunbohuiApihttps(object):
    def __init__(self):
        self.base_url = CONFIG.HUNBOHUI_BASE_URL_HTTPS
        self.session = make_session()


    @request(url='lottery/get-lottery', method='post')
    def get_lottery_list(self, lottery_id):
        """
        查看惊爆大抽奖,id=1这个活动的奖品列表
        """

        json = {
            "lottery_id": lottery_id
        }
        headers = {
            "Host": 'open.test.jiehun.com.cn',
            "Connection": 'keep-alive',
            "Accept": 'application/json, text/plain, */*',
            "Origin": 'http://act.test.jiehun.com.cn',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "Content-Type": 'application/json; charset=UTF-8',
            "Accept-Encoding": 'gzip, deflate',
            "Accept-Language": 'zh-CN,en-US;q=0.8',
            "X-Requested-With": 'com.china.hunbohui',
            "Referer":"http://act.test.jiehun.com.cn/choujiang/?lottery_id=1"
        }
        return response(json=json, headers=headers,verify=False)

    @request(url='lottery/get-winner-list', method='post')
    def get_winner_list(self, lottery_id, pageNum, pageSize):
        """
        查看惊爆大抽奖,id=1这个活动的中奖名单
        """

        json = {
            "lottery_id": lottery_id,
            "pageNum": pageNum,
            "pageSize": pageSize
        }
        headers = {
            "Host": 'open.test.jiehun.com.cn',
            "Connection": 'keep-alive',
            "Accept": 'application/json, text/plain, */*',
            "Origin": 'http://act.test.jiehun.com.cn',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "Content-Type": 'application/json; charset=UTF-8',
            "Accept-Encoding": 'gzip, deflate',
            "Accept-Language": 'zh-CN,en-US;q=0.8',
            "X-Requested-With": 'com.china.hunbohui',
            "Referer": "http://act.test.jiehun.com.cn/choujiang/?lottery_id=1"
        }
        return response(json=json, headers=headers, verify=False)