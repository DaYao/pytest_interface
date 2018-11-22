import requests
# from common import config


host = 'http://172.16.200.100:5000'
# host = 'http://127.0.0.1:5000'


class DataAddCount(object):
    def __init__(self):
        self.base_url = host
        self.header = {
            'Content-Type': 'application/json'
        }

    def dmp_base_brand_data_count(self):
        query = '/mock/count'
        headers = self.header
        json = {
            'operation': 'add',
            'usertoken':'LS2Amesk0HFLRzJN66FgZ8d0EGMTxd3Y'
        }
        res = requests.post(url=self.base_url + query, headers=headers, json=json,
                             allow_redirects=False)
        res_json = res.json()
        return res_json['msg']['count']


class DataGetCount(object):
    def __init__(self):
        self.base_url = host
        self.header = {
            'Content-Type': 'application/json'
        }

    def get_dmp_base_brand_data_count(self):
        query = '/mock/count'
        headers = self.header
        params = {
            'usertoken':'LS2Amesk0HFLRzJN66FgZ8d0EGMTxd3Y'
        }
        res = requests.get(url=self.base_url + query, headers=headers, params=params,
                             allow_redirects=False)
        res_json = res.json()
        return res_json['msg']['count']




if __name__ == '__main__':
    # data_count = DataAddCount()
    # print(data_count.dmp_base_brand_data_count())
    data_get_count = DataGetCount()
    print(data_get_count.get_dmp_base_brand_data_count())
    # print(data_get_count.get_customer_data_count())
    # print(data_get_count.get_floor_data_count())
    # print(data_get_count.get_floor_data_count())
    # print(data_get_count.get_floor_data_count())