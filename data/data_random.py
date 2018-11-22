import requests

DATA_HOST = 'http://172.16.6.52:5001'

class DataRandom(object):

    def __init__(self):
        self.base_url = DATA_HOST
        self.header = {
            'Content-Type': 'application/json'
        }
        self.query = '/mock/random'

    def random_name(self):
        query = self.query
        headers = self.header
        params = {
            'data': 'name'
        }
        res = requests.get(url=self.base_url + query, headers=headers, params=params,
                            allow_redirects=False)
        res_json = res.json()
        return res_json['msg']['name']

    def random_Englishname(self):
        query = self.query
        headers = self.header
        params = {
            'data': 'Englishname'
        }
        res = requests.get(url=self.base_url + query, headers=headers, params=params,
                            allow_redirects=False)
        res_json = res.json()
        return res_json['msg']['Englishname']

    def random_phone(self):
        query = self.query
        headers = self.header
        params = {
            'data': 'phone'
        }
        res = requests.get(url=self.base_url + query, headers=headers, params=params,
                            allow_redirects=False)
        res_json = res.json()
        return res_json['msg']['phone']

    def random_address(self):
        query = self.query
        headers = self.header
        params = {
            'data': 'address'
        }
        res = requests.get(url=self.base_url + query, headers=headers, params=params,
                            allow_redirects=False)
        res_json = res.json()
        return res_json['msg']['address']

if __name__ == '__main__':
    data_random = DataRandom()
    print(data_random.random_address())
    print(data_random.random_name())
    print(data_random.random_phone())