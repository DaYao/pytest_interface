# @Time    :2018/11/19 9:29
# @Author  :lvjunjie

from common.api import request, response, make_session
from utils.cfg import CONFIG

class FreeTicket(object):


    def __init__(self):
        self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
        self.session = make_session()
        self.session.header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
        self.base_url = CONFIG.MDP_BASE_URL


    @request(method='get')
    def free_ticket_index(self, city):
        url = 'http://' + city + '.expo.jiehun.com.cn/'

        return {"url": url, "headers": self.session.header}

    @request(method='get')
    def free_ticket_expo_index(self, city):
        url = 'http://' + city + '.expo.jiehun.com.cn/m/expo'

        return {"url": url, "headers": self.session.header}

    @request(method='post')
    def free_ticket_save_inputphone(self, city):
        url = 'https://' + city + '.jiehun.com.cn/expo/new_ticket/_save'
        data = {
            "step": 1,
            "city_id": 330100,
            "project_id": 4,
            "expo_type": 1,
            "t_form_id": 231,
            "old_form": 1,
            "ticket_count": 4546,
            "zt_id": 21478,
            "name": "123",
            "spouse_name": "测试",
            "address": "我是测试地址",
            "re_phone": "Orf1JK/5k63LnzNVYUunY3mJ8sbXP4lodt3h6OBaAbvVlJmsbQC/spzBTOk1sfox7+J3u7isdc3ReCzNqIS5W8raId7yuO4OEeOiWeInplbZ9X9RupS9Xpn7dLB+3cLBlWqJZF4MUD/EO8sEFGrkQxT9hpM8jc9vyHhNJJUMJxQ=",
            # "spouse_phone": spouse_phone
        }
        return {"url": url, "data":data, "headers": self.session.header}


if __name__ == '__main__':
    free_ticker = FreeTicket()
    # res = free_ticker.free_ticket_expo_index('tj')
    # print(res.text)
    res = free_ticker.free_ticket_save_inputphone('hz')
    print(res.text)
