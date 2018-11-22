# coding=utf-8
from pithy import request, response, make_session
from utils.cfg import CONFIG


class HunbohuiApi(object):
    def __init__(self):
        self.base_url = CONFIG.HUNBOHUI_BASE_URL_HTTP
        self.session = make_session()

    @request(url='user/account/get-login', method='post')
    def login(self, username, password, client_id):
        """
        账号密码登录
        """
        json = {
            "username": username,
            "password": password,
            "client_id":client_id
        }
        headers = {
            "city-id":'330100',
            "device-id":'865223034945792',
            "site-city-name":'330100',
            "app-visit-path":'normal/mine/AccountLoginActivity',
            "client-id":'205',
            "User-Agent":'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name":'%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "page-id":'47cb0a5a-1086-47e0-a10d-4ab2459f3e20',
            "app-id":'10000',
            "app-key":'hunbasha_android',
            "view-id":'7f9b1651-6331-43ac-8add-e4ccc2f9a26e',
            "app-channel":'hunbohui',
            "app-version":'6.1.0',
            "Content-Type": 'application/json; charset=UTF-8',
            "Host":'open.test.jiehun.com.cn',
            "Accept-Encoding":'gzip',
            "Connection":'keep-alive'
        }
        return response(json=json, headers=headers)

    def loginfirst(self, username, password, client_id):
        """获取登录基本参数"""
        res = self.login(username, password, client_id).json
        ak = res.data.access_token
        self.session.headers['Authorization'] = 'dmp ' + ak

    @request(url='user/account/post-sent-sms', method='post')
    def sent_sms(self, phone):
        """
        手机快捷登录，发送验证码
        """

        json = {
            "phone": phone,
        }
        headers = {
            "city-id": '330100',
            "device-id": '865223034945792',
            "site-city-name": '330100',
            "app-visit-path": 'normal/mine/login',
            "client-id": '205',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "page-id": '47cb0a5a-1086-47e0-a10d-4ab2459f3e20',
            "app-id": '10000',
            "app-key": 'hunbasha_android',
            "view-id": '7f9b1651-6331-43ac-8add-e4ccc2f9a26e',
            "app-channel": 'hunbohui',
            "app-version": '6.1.0',
            "Content-Type": 'application/json; charset=UTF-8',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip',
            "Connection": 'keep-alive'
        }
        return response(json=json, headers=headers)

    @request(url='user/account/post-code-login', method='post')
    def login_code(self, phone, code, client_id):
        """
        手机快捷登录
        """

        json = {
            "phone": phone,
            "code": code,
            "client_id": client_id
        }
        headers = {
            "city-id": '330100',
            "device-id": '865223034945792',
            "site-city-name": '330100',
            "app-visit-path": 'normal/mine/AccountLoginActivity',
            "client-id": '205',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "page-id": '47cb0a5a-1086-47e0-a10d-4ab2459f3e20',
            "app-id": '10000',
            "app-key": 'hunbasha_android',
            "view-id": '7f9b1651-6331-43ac-8add-e4ccc2f9a26e',
            "app-channel": 'hunbohui',
            "app-version": '6.1.0',
            "Content-Type": 'application/json; charset=UTF-8',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip',
            "Connection": 'keep-alive'
        }
        return response(json=json, headers=headers)

    @request(url='user/account/post-change-pwd', method='post')
    def login_forgot_pwd(self, phone, pwd, code, confirm_pwd):
        """
        忘记密码页面，修改密码
        """

        json = {
            "phone": phone,
            "pwd": pwd,
            "code": code,
            "confirm_pwd": confirm_pwd
        }
        headers = {
            "city-id": '330100',
            "device-id": '865223034945792',
            "site-city-name": '330100',
            "app-visit-path": 'normal/mine/account_login/retrieve',
            "client-id": '205',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "page-id": '47cb0a5a-1086-47e0-a10d-4ab2459f3e20',
            "app-id": '10000',
            "app-key": 'hunbasha_android',
            "view-id": '7f9b1651-6331-43ac-8add-e4ccc2f9a26e',
            "app-channel": 'hunbohui',
            "app-version": '6.1.0',
            "Content-Type": 'application/json; charset=UTF-8',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip',
            "Connection": 'keep-alive'
        }
        return response(json=json, headers=headers)

    @request(url='user/account/post-change-pwd', method='post')
    def login_change_pwd(self, phone, pwd, code):
        """
        修改密码页面，修改密码
        """

        json = {
            "phone": phone,
            "pwd": pwd,
            "code": code,
        }
        headers = {
            "city-id": '330100',
            "device-id": '865223034945792',
            "site-city-name": '330100',
            "app-visit-path": 'normal/mine/account_login/retrieve',
            "client-id": '205',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "page-id": '47cb0a5a-1086-47e0-a10d-4ab2459f3e20',
            "app-id": '10000',
            "app-key": 'hunbasha_android',
            "view-id": '7f9b1651-6331-43ac-8add-e4ccc2f9a26e',
            "app-channel": 'hunbohui',
            "app-version": '6.1.0',
            "Content-Type": 'application/json; charset=UTF-8',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip',
            "Connection": 'keep-alive'
        }
        return response(json=json, headers=headers)

    @request(url='coupon/get-list', method='post')
    def coupon_list(self, pageNum, pageSize, industryName):
        """
        现金券列表
        """

        json = {
            "pageNum": pageNum,
            "pageSize": pageSize,
            "industryName": industryName

        }
        headers = {
            "city-id": '330100',
            "device-id": '865223034945792',
            "site-city-name": '330100',
            "app-visit-path": 'normal/mine/AccountLoginActivity',
            "client-id": '205',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "page-id": '47cb0a5a-1086-47e0-a10d-4ab2459f3e20',
            "app-id": '10000',
            "app-key": 'hunbasha_android',
            "view-id": '7f9b1651-6331-43ac-8add-e4ccc2f9a26e',
            "app-channel": 'hunbohui',
            "app-version": '6.1.0',
            "Content-Type": 'application/json; charset=UTF-8',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip',
            "Connection": 'keep-alive'
        }
        return response(json=json, headers=headers)

    @request(url='user/coupon/post-coupon', method='post')
    def post_coupon(self, marketingCouponId):
        """
        免费领取现金券
        """

        json = {
            "marketingCouponId": marketingCouponId

        }
        headers = {
            "city-id": '330100',
            "device-id": '865223034945792',
            "site-city-name": '330100',
            "app-visit-path": 'normal/mine/AccountLoginActivity',
            "client-id": '205',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "page-id": '47cb0a5a-1086-47e0-a10d-4ab2459f3e20',
            "app-id": '10000',
            "app-key": 'hunbasha_android',
            "view-id": '7f9b1651-6331-43ac-8add-e4ccc2f9a26e',
            "app-channel": 'hunbohui',
            "app-version": '6.1.0',
            "Content-Type": 'application/json; charset=UTF-8',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip',
            "Connection": 'keep-alive',
            "Authorization":'dmp ARRNOLiM9awOB1d5fCH9HVgaGjisjPWsDANUYnwu4R9LBhZn/oLt+lRZA253KfoeSgYBYOyb/KIfXAQkEnGrD0AUCmXqn/25BA1EMWss/kkbBl1k7pj6vFgMX3h0ff8UHAMLabrP/eoPUlQpLw=='
        }
        return response(json=json, headers=headers)

    @request(url='my/address/get-default-addr', method='post')
    def my_address(self):
        """
        点击头像查看我的资料
        """

        json = {
        }
        headers = {
            "city-id": '330100',
            "device-id": '0D558C15-95D5-4520-90C4-189788018BE8',
            "site-city-name": '',
            "app-visit-path": 'normal/mine/my_profile',
            "client-id": '844',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name": '',
            "page-id": '01E9AED0-E324-4787-93A5-E8D810AAF4F4',
            "app-id": '10000',
            "app-key": 'hunbasha_ios',
            "view-id": '7f9b1651-6331-43ac-8add-e4ccc2f9a26e',
            "app-channel": 'App Store',
            "app-version": '6.10',
            "Content-Type": 'application/json',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip;q=1.0, compress;q=0.5',
            "Connection": 'keep-alive'
        }
        return response(json=json, headers=headers)

    @request(url='mobile/get-channel', method='post')
    def get_channel(self):
        """
        查看首页
        """

        json = {
        }
        headers = {
            "city-id": '110900',
            "device-id": 'AC153270-FBCE-4754-8F2C-3BB1A8F22A5A',
            "site-city-name": '',
            "app-visit-path": 'normal/home',
            "client-id": '858',
            "User-Agent": 'WeddingBazaar/6.10 (iss.HunBoHui; build:1; iOS 10.1.1) Alamofire/4.7.2',
            "visit-city-name": '',
            "envCode":'',
            "page-id": '01E9AED0-E324-4787-93A5-E8D810AAF4F4',
            "app-id": '10000',
            "app-key": 'hunbasha_ios',
            "view-id": '3D95554C-0BC8-4F48-B330-0ABF0120C7F0',
            "app-channel": 'App Store',
            "app-version": '6.10',
            "Content-Type": 'application/json',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip;q=1.0, compress;q=0.5',
            "Accept-Language":'zh-Hans-CN;q=1.0',
            "Connection": 'keep-alive'
        }
        return response(json=json, headers=headers)

    @request(url='mobile/get-channel', method='post')
    def get_channel_detail(self, channel):
        """
        查看首页，点击查看婚纱摄影
        """

        json = {
            "channel": channel
        }
        headers = {
            "city-id": '110900',
            "device-id": 'AC153270-FBCE-4754-8F2C-3BB1A8F22A5A',
            "site-city-name": '',
            "app-visit-path": 'normal/home',
            "client-id": '858',
            "User-Agent": 'WeddingBazaar/6.10 (iss.HunBoHui; build:1; iOS 10.1.1) Alamofire/4.7.2',
            "visit-city-name": '',
            "envCode": '',
            "page-id": '01E9AED0-E324-4787-93A5-E8D810AAF4F4',
            "app-id": '10000',
            "app-key": 'hunbasha_ios',
            "view-id": '3D95554C-0BC8-4F48-B330-0ABF0120C7F0',
            "app-channel": 'App Store',
            "app-version": '6.10',
            "Content-Type": 'application/json',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip;q=1.0, compress;q=0.5',
            "Accept-Language": 'zh-Hans-CN;q=1.0',
            "Connection": 'keep-alive'
        }
        return response(json=json, headers=headers)

    @request(url='store/get-storelist', method='post')
    def get_storelist(self, industryCateId, pageNum, pageSize):
        """
        首页点击行业查看
        """

        json = {
            "industryCateId": industryCateId,
            "pageNum": pageNum,
            "pageSize":pageSize
        }
        headers = {
            "city-id": '110900',
            "device-id": '0D558C15-95D5-4520-90C4-189788018BE8',
            "site-city-name": '',
            "app-visit-path": 'normal/mine/my_profile',
            "client-id": '844',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name": '',
            "page-id": '01E9AED0-E324-4787-93A5-E8D810AAF4F4',
            "app-id": '10000',
            "app-key": 'hunbasha_ios',
            "view-id": '7f9b1651-6331-43ac-8add-e4ccc2f9a26e',
            "app-channel": 'App Store',
            "app-version": '6.10',
            "Content-Type": 'application/json',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip;q=1.0, compress;q=0.5',
            "Connection": 'keep-alive'
        }
        return response(json=json, headers=headers)

    @request(url='store/get-detail', method='post')
    def get_store_detail(self, latitude, storeId, longitude):
        """
        点击查看店铺详情
        """

        json = {
            "latitude": latitude,
            "storeId": storeId,
            "longitude": longitude
        }
        headers = {
            "city-id": '110900',
            "device-id": 'AC153270-FBCE-4754-8F2C-3BB1A8F22A5A',
            "site-city-name": '',
            "app-visit-path": 'normal/home/channel/store_list/store_datail',
            "client-id": '858',
            "User-Agent": 'WeddingBazaar/6.10 (iss.HunBoHui; build:1; iOS 10.1.1) Alamofire/4.7.2',
            "visit-city-name": '',
            "envCode": '',
            "page-id": '01E9AED0-E324-4787-93A5-E8D810AAF4F4',
            "app-id": '10000',
            "app-key": 'hunbasha_ios',
            "view-id": '3D95554C-0BC8-4F48-B330-0ABF0120C7F0',
            "app-channel": 'App Store',
            "app-version": '6.10',
            "Content-Type": 'application/json',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip;q=1.0, compress;q=0.5',
            "Accept-Language": 'zh-Hans-CN;q=1.0',
            "Connection": 'keep-alive'
        }
        return response(json=json, headers=headers)

    @request(url='product/get-detail', method='post')
    def get_product_detail(self, productId, cityName):
        """
        点击查看商品详情
        """

        json = {
            "productId": productId,
            "cityName": cityName
        }
        headers = {
            "city-id": '110900',
            "device-id": 'AC153270-FBCE-4754-8F2C-3BB1A8F22A5A',
            "site-city-name": '',
            "app-visit-path": 'normal/home/channel/store_list/store_datail/product_detail',
            "client-id": '858',
            "User-Agent": 'WeddingBazaar/6.10 (iss.HunBoHui; build:1; iOS 10.1.1) Alamofire/4.7.2',
            "visit-city-name": '',
            "envCode": '',
            "page-id": '01E9AED0-E324-4787-93A5-E8D810AAF4F4',
            "app-id": '10000',
            "app-key": 'hunbasha_ios',
            "view-id": '3D95554C-0BC8-4F48-B330-0ABF0120C7F0',
            "app-channel": 'App Store',
            "app-version": '6.10',
            "Content-Type": 'application/json',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip;q=1.0, compress;q=0.5',
            "Accept-Language": 'zh-Hans-CN;q=1.0',
            "Connection": 'keep-alive'
        }
        return response(json=json, headers=headers)

    @request(url='my/follow/post-save', method='post')
    def get_my_follow_postsave(self, item_type, item_ids, mode):
        """
        收藏商品
        """

        json = {
            "item_type": item_type,
            "item_ids": item_ids,
            "mode":mode
        }
        headers = {
            "city-id": '110900',
            "device-id": 'AC153270-FBCE-4754-8F2C-3BB1A8F22A5A',
            "site-city-name": '',
            "app-visit-path": 'normal/home/channel/store_list/store_datail/product_detail',
            "client-id": '858',
            "User-Agent": 'WeddingBazaar/6.10 (iss.HunBoHui; build:1; iOS 10.1.1) Alamofire/4.7.2',
            "visit-city-name": '',
            "envCode": '',
            "page-id": '01E9AED0-E324-4787-93A5-E8D810AAF4F4',
            "app-id": '10000',
            "app-key": 'hunbasha_ios',
            "view-id": '3D95554C-0BC8-4F48-B330-0ABF0120C7F0',
            "app-channel": 'App Store',
            "app-version": '6.10',
            "Content-Type": 'application/json',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip;q=1.0, compress;q=0.5',
            "Accept-Language": 'zh-Hans-CN;q=1.0',
            "Connection": 'keep-alive'
        }
        return response(json=json, headers=headers)

    @request(url='search/get-list', method='post')
    def get_search_list(self, keywords):
        """
        通过搜索获得列表
        """

        json = {
            "keywords": keywords
        }
        headers = {
            "city-id": '110900',
            "device-id": 'AC153270-FBCE-4754-8F2C-3BB1A8F22A5A',
            "site-city-name": '',
            "app-visit-path": 'normal/home/search',
            "client-id": '858',
            "User-Agent": 'WeddingBazaar/6.10 (iss.HunBoHui; build:1; iOS 10.1.1) Alamofire/4.7.2',
            "visit-city-name": '',
            "envCode": '',
            "page-id": '01E9AED0-E324-4787-93A5-E8D810AAF4F4',
            "app-id": '10000',
            "app-key": 'hunbasha_ios',
            "view-id": '3D95554C-0BC8-4F48-B330-0ABF0120C7F0',
            "app-channel": 'App Store',
            "app-version": '6.10',
            "Content-Type": 'application/json',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip;q=1.0, compress;q=0.5',
            "Accept-Language": 'zh-Hans-CN;q=1.0',
            "Connection": 'keep-alive'
        }
        return response(json=json, headers=headers)

    @request(url='message/notice/get-c-cate-list', method='post')
    def get_notice_list(self, uid):
        """
        首页点击查看消息列表
        """

        json = {
            "uid": uid
        }
        headers = {
            "city-id": '330100',
            "device-id": '865223034945792',
            "site-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "resolution":'1280X720',
            "os-name":'Android',
            "app-visit-path": 'normal/MainTabActivity/my_message_list',
            "client-id": '205',
            "os-version":'6.0.1',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "page-id": 'ecf8f07a-5ea2-4b12-9dcf-eb30660fc466',
            "app-id": '10000',
            "app-key": 'hunbasha_android',
            "view-id": '7f9b1651-6331-43ac-8add-e4ccc2f9a26e',
            "app-channel": 'hunbohui',
            "app-version": '6.3.0',
            "Content-Type": 'application/json',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip;q=1.0, compress;q=0.5',
            "Connection": 'keep-alive',
            "Authorization": 'dmp ARRNOLiM9awOB1d5fCH9HVgaGjisjPWsDANUYnwu4R9LBhZn/oLt+lRZA253KfoeSQ4OaOqb96IfXAQkEnGrD0AUCmXqn/25BA1EMWt6rh1OBQE06Mr4vAwEUS4rK6xIHAJdNOnP971YUAB8Kw=='
        }
        return response(json=json, headers=headers)

    @request(url='order/ordercart/get-product', method='post')
    def get_product(self, industryCateId):
        """
        查看购物车
        """

        json = {
            "industryCateId": industryCateId

        }
        headers = {
            "city-id": '330100',
            "device-id": '865223034945792',
            "site-city-name": '330100',
            "app-visit-path": 'normal/mine/order_cart',
            "client-id": '205',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "page-id": '47cb0a5a-1086-47e0-a10d-4ab2459f3e20',
            "app-id": '10000',
            "app-key": 'hunbasha_android',
            "view-id": 'a9b6a3c7-39d5-476f-917f-1c99f5243c8a',
            "app-channel": 'hunbohui',
            "app-version": '6.1.0',
            "Content-Type": 'application/json; charset=UTF-8',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip',
            "Connection": 'keep-alive',
            "Authorization": 'dmp ARRNOLiM9awOB1d5fCH9HVgaGjisjPWsDANUYnwu4R9LBhZn/oLt+lRZA253KfoeSQ4OaOqb96IfXAQkEnGrD0AUCmXqn/25BA1EMWt6rh1OBQE06Mr4vAwEUS4rK6xIHAJdNOnP971YUAB8Kw=='
        }
        return response(json=json, headers=headers)

    @request(url='order/get-page-order', method='post')
    def get_order(self, orderStatus, pageNum, pageSize):
        """
        查看我的订单
        """

        json = {
            # orderStatus  1代表待付款；2代表待完成；3代表已完成；空代表全部
            "orderStatus": orderStatus,
            "pageNum": pageNum,
            "pageSize": pageSize
        }
        headers = {
            "city-id": '330100',
            "device-id": '865223034945792',
            "site-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "app-visit-path": 'normal/mine/order_list',
            "client-id": '205',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "page-id": '47cb0a5a-1086-47e0-a10d-4ab2459f3e20',
            "app-id": '10000',
            "app-key": 'hunbasha_android',
            "view-id": 'a9b6a3c7-39d5-476f-917f-1c99f5243c8a',
            "app-channel": 'hunbohui',
            "app-version": '6.1.0',
            "Content-Type": 'application/json; charset=UTF-8',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip',
            "Connection": 'keep-alive',
            "Authorization": 'dmp ARRNOLiM9awOB1d5fCH9HVgaGjisjPWsDANUYnwu4R9LBhZn/oLt+lRZA253KfoeSQ4OaOqb96IfXAQkEnGrD0AUCmXqn/25BA1EMWt6rh1OBQE06Mr4vAwEUS4rK6xIHAJdNOnP971YUAB8Kw=='
        }
        return response(json=json, headers=headers)

    @request(url='mall/dp/get-list-user', method='post')
    def get_list_user(self, Status):
        """
        查看我的评价
        """

        json = {
            # Status  0代表待评价；1代表待追加；10代表已完成
            "Status": Status
        }
        headers = {
            "city-id": '330100',
            "device-id": '865223034945792',
            "site-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "app-visit-path": 'normal/mine/comment_list',
            "client-id": '205',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "page-id": '47cb0a5a-1086-47e0-a10d-4ab2459f3e20',
            "app-id": '10000',
            "app-key": 'hunbasha_android',
            "view-id": 'a9b6a3c7-39d5-476f-917f-1c99f5243c8a',
            "app-channel": 'hunbohui',
            "app-version": '6.1.0',
            "Content-Type": 'application/json; charset=UTF-8',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip',
            "Connection": 'keep-alive',
            "Authorization": 'dmp ARRNOLiM9awOB1d5fCH9HVgaGjisjPWsDANUYnwu4R9LBhZn/oLt+lRZA253KfoeSQ4OaOqb96IfXAQkEnGrD0AUCmXqn/25BA1EMWt6rh1OBQE06Mr4vAwEUS4rK6xIHAJdNOnP971YUAB8Kw=='
        }
        return response(json=json, headers=headers)

    @request(url='zone/ucenter/get-ucenter', method='post')
    def get_ucenter(self, type, pageNum, pageSize):
        """
        查看我的社区
        """

        json = {
            "type": type,
            "pageNum": pageNum,
            "pageSize": pageSize
        }
        headers = {
            "city-id": '330100',
            "device-id": '865223034945792',
            "site-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "app-visit-path": 'normal/mine/bbs_person_center',
            "client-id": '205',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "page-id": '47cb0a5a-1086-47e0-a10d-4ab2459f3e20',
            "app-id": '10000',
            "app-key": 'hunbasha_android',
            "view-id": 'a9b6a3c7-39d5-476f-917f-1c99f5243c8a',
            "app-channel": 'hunbohui',
            "app-version": '6.1.0',
            "Content-Type": 'application/json; charset=UTF-8',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip',
            "Connection": 'keep-alive',
            "Authorization": 'dmp ARRNOLiM9awOB1d5fCH9HVgaGjisjPWsDANUYnwu4R9LBhZn/oLt+lRZA253KfoeSgYBYOyb/KIfXAQkEnGrD0AUCmXqn/25BA1EMWss/kkbBl1k7pj6vFgMX3h0ff8UHAMLabrP/eoPUlQpLw=='
        }
        return response(json=json, headers=headers)

    @request(url='zone/section/get-home', method='post')
    def get_zone_section(self, pageNum):
        """
        点击查看“结婚攻略”页面
        """

        json = {
            "pageNum": pageNum
        }
        headers = {
            "city-id": '330100',
            "device-id": '865223034945792',
            "site-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "app-visit-path": 'normal/bbs_home',
            "client-id": '205',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "page-id": '47cb0a5a-1086-47e0-a10d-4ab2459f3e20',
            "app-id": '10000',
            "app-key": 'hunbasha_android',
            "view-id": 'a9b6a3c7-39d5-476f-917f-1c99f5243c8a',
            "app-channel": 'hunbohui',
            "app-version": '6.1.0',
            "Content-Type": 'application/json; charset=UTF-8',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip',
            "Connection": 'keep-alive',
            "Authorization": 'dmp ARRNOLiM9awOB1d5fCH9HVgaGjisjPWsDANUYnwu4R9LBhZn/oLt+lRZA253KfoeSgYBYOyb/KIfXAQkEnGrD0AUCmXqn/25BA1EMWss/kkbBl1k7pj6vFgMX3h0ff8UHAMLabrP/eoPUlQpLw=='
        }
        return response(json=json, headers=headers)

    @request(url='zone/section/get-list', method='post')
    def get_zone_section_list(self, pageNum, section_id, pageSize):
        """
        点击"查看更多"跳转到栏目全部内容
        """

        json = {
            "pageNum": pageNum,
            "section_id": section_id,
            "pageSize": pageSize
        }
        headers = {
            "city-id": '330100',
            "device-id": '865223034945792',
            "site-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "app-visit-path": 'normal/bbs_home/bbs_strategy_column',
            "client-id": '205',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "page-id": '47cb0a5a-1086-47e0-a10d-4ab2459f3e20',
            "app-id": '10000',
            "app-key": 'hunbasha_android',
            "view-id": 'a9b6a3c7-39d5-476f-917f-1c99f5243c8a',
            "app-channel": 'hunbohui',
            "app-version": '6.1.0',
            "Content-Type": 'application/json; charset=UTF-8',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip',
            "Connection": 'keep-alive',
            "Authorization": 'dmp ARRNOLiM9awOB1d5fCH9HVgaGjisjPWsDANUYnwu4R9LBhZn/oLt+lRZA253KfoeSgYBYOyb/KIfXAQkEnGrD0AUCmXqn/25BA1EMWss/kkbBl1k7pj6vFgMX3h0ff8UHAMLabrP/eoPUlQpLw=='
        }
        return response(json=json, headers=headers)

    @request(url='zone/gonglve/get-detail', method='post')
    def get_zone_gonglve_detail(self, is_wap, pageNum, community_id, pageSize):
        """
        栏目全部内容,点击查看第一个攻略页面
        """

        json = {
            "is_wap": is_wap,
            "pageNum": pageNum,
            "community_id": community_id,
            "pageSize": pageSize
        }
        headers = {
            "city-id": '330100',
            "device-id": '865223034945792',
            "site-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "app-visit-path": 'normal/bbs_home/bbs_strategy_column/bbs_strategy_detail',
            "client-id": '205',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "page-id": '47cb0a5a-1086-47e0-a10d-4ab2459f3e20',
            "app-id": '10000',
            "app-key": 'hunbasha_android',
            "view-id": 'a9b6a3c7-39d5-476f-917f-1c99f5243c8a',
            "app-channel": 'hunbohui',
            "app-version": '6.1.0',
            "Content-Type": 'application/json; charset=UTF-8',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip',
            "Connection": 'keep-alive',
            "Authorization": 'dmp ARRNOLiM9awOB1d5fCH9HVgaGjisjPWsDANUYnwu4R9LBhZn/oLt+lRZA253KfoeSgYBYOyb/KIfXAQkEnGrD0AUCmXqn/25BA1EMWss/kkbBl1k7pj6vFgMX3h0ff8UHAMLabrP/eoPUlQpLw=='
        }
        return response(json=json, headers=headers)

    @request(url='zone/topic/post-collect', method='post')
    def post_zone_topic_collect(self, type, community_id):
        """
        第一个攻略页面，点击收藏
        """

        json = {
            "type": type,
            "community_id": community_id
        }
        headers = {
            "city-id": '330100',
            "device-id": '865223034945792',
            "site-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "app-visit-path": 'normal/bbs_home/bbs_strategy_column/bbs_strategy_detail',
            "client-id": '205',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "page-id": '47cb0a5a-1086-47e0-a10d-4ab2459f3e20',
            "app-id": '10000',
            "app-key": 'hunbasha_android',
            "view-id": 'a9b6a3c7-39d5-476f-917f-1c99f5243c8a',
            "app-channel": 'hunbohui',
            "app-version": '6.1.0',
            "Content-Type": 'application/json; charset=UTF-8',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip',
            "Connection": 'keep-alive',
            "Authorization": 'dmp ARRNOLiM9awOB1d5fCH9HVgaGjisjPWsDANUYnwu4R9LBhZn/oLt+lRZA253KfoeSgYBYOyb/KIfXAQkEnGrD0AUCmXqn/25BA1EMWss/kkbBl1k7pj6vFgMX3h0ff8UHAMLabrP/eoPUlQpLw=='
        }
        return response(json=json, headers=headers)

    @request(url='zone/topic/post-support', method='post')
    def post_zone_topic_support(self, type, community_id):
        """
        第一个攻略页面，点击点赞
        """

        json = {
            "type": type,
            "community_id": community_id
        }
        headers = {
            "city-id": '330100',
            "device-id": '865223034945792',
            "site-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "app-visit-path": 'normal/bbs_home/bbs_strategy_column/bbs_strategy_detail',
            "client-id": '205',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "page-id": '47cb0a5a-1086-47e0-a10d-4ab2459f3e20',
            "app-id": '10000',
            "app-key": 'hunbasha_android',
            "view-id": 'a9b6a3c7-39d5-476f-917f-1c99f5243c8a',
            "app-channel": 'hunbohui',
            "app-version": '6.1.0',
            "Content-Type": 'application/json; charset=UTF-8',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip',
            "Connection": 'keep-alive',
            "Authorization": 'dmp ARRNOLiM9awOB1d5fCH9HVgaGjisjPWsDANUYnwu4R9LBhZn/oLt+lRZA253KfoeSgYBYOyb/KIfXAQkEnGrD0AUCmXqn/25BA1EMWss/kkbBl1k7pj6vFgMX3h0ff8UHAMLabrP/eoPUlQpLw=='
        }
        return response(json=json, headers=headers)

    @request(url='zone/gonglve/get-recommend', method='post')
    def get_zone_gonglve_recommend(self, community_id):
        """
        第一个攻略页面，点击全部推荐
        """

        json = {
            "community_id": community_id
        }
        headers = {
            "city-id": '330100',
            "device-id": '865223034945792',
            "site-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "app-visit-path": 'normal/bbs_home/bbs_strategy_column/bbs_strategy_detail',
            "client-id": '205',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "page-id": '47cb0a5a-1086-47e0-a10d-4ab2459f3e20',
            "app-id": '10000',
            "app-key": 'hunbasha_android',
            "view-id": 'a9b6a3c7-39d5-476f-917f-1c99f5243c8a',
            "app-channel": 'hunbohui',
            "app-version": '6.1.0',
            "Content-Type": 'application/json; charset=UTF-8',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip',
            "Connection": 'keep-alive',
            "Authorization": 'dmp ARRNOLiM9awOB1d5fCH9HVgaGjisjPWsDANUYnwu4R9LBhZn/oLt+lRZA253KfoeSgYBYOyb/KIfXAQkEnGrD0AUCmXqn/25BA1EMWss/kkbBl1k7pj6vFgMX3h0ff8UHAMLabrP/eoPUlQpLw=='
        }
        return response(json=json, headers=headers)

    @request(url='zone/reply/post-reply', method='post')
    def post_zone_reply(self, content, community_id):
        """
        第一个攻略页面，添加评论
        """

        json = {
            "content": content,
            "community_id": community_id
        }
        headers = {
            "city-id": '330100',
            "device-id": '865223034945792',
            "site-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "app-visit-path": 'normal/bbs_home/bbs_strategy_column/bbs_strategy_detail/bbs_comment_post',
            "client-id": '205',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "page-id": '47cb0a5a-1086-47e0-a10d-4ab2459f3e20',
            "app-id": '10000',
            "app-key": 'hunbasha_android',
            "view-id": 'a9b6a3c7-39d5-476f-917f-1c99f5243c8a',
            "app-channel": 'hunbohui',
            "app-version": '6.1.0',
            "Content-Type": 'application/json; charset=UTF-8',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip',
            "Connection": 'keep-alive',
            "Authorization": 'dmp ARRNOLiM9awOB1d5fCH9HVgaGjisjPWsDANUYnwu4R9LBhZn/oLt+lRZA253KfoeSgYBYOyb/KIfXAQkEnGrD0AUCmXqn/25BA1EMWss/kkbBl1k7pj6vFgMX3h0ff8UHAMLabrP/eoPUlQpLw=='
        }
        return response(json=json, headers=headers)

    @request(url='zone/reply/get-comments', method='post')
    def get_zone_reply_comments(self, pageNum, reply_id, pageSize):
        """
        第一个攻略页面，对第一个评论进行点击查看详情
        """

        json = {
            "pageNum": pageNum,
            "reply_id": reply_id,
            "pageSize": pageSize
        }
        headers = {
            "city-id": '330100',
            "device-id": '865223034945792',
            "site-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "app-visit-path": 'normal/bbs_home/bbs_strategy_column/bbs_strategy_detail/answer_detail',
            "client-id": '205',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "page-id": '47cb0a5a-1086-47e0-a10d-4ab2459f3e20',
            "app-id": '10000',
            "app-key": 'hunbasha_android',
            "view-id": 'a9b6a3c7-39d5-476f-917f-1c99f5243c8a',
            "app-channel": 'hunbohui',
            "app-version": '6.1.0',
            "Content-Type": 'application/json; charset=UTF-8',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip',
            "Connection": 'keep-alive',
            "Authorization": 'dmp ARRNOLiM9awOB1d5fCH9HVgaGjisjPWsDANUYnwu4R9LBhZn/oLt+lRZA253KfoeSgYBYOyb/KIfXAQkEnGrD0AUCmXqn/25BA1EMWss/kkbBl1k7pj6vFgMX3h0ff8UHAMLabrP/eoPUlQpLw=='
        }
        return response(json=json, headers=headers)

    @request(url='zone/reply/post-support', method='post')
    def post_zone_reply_support(self, type, reply_id):
        """
        第一个攻略页面，对第一个评论进行点赞
        """

        json = {
            "type": type,
            "reply_id": reply_id
        }
        headers = {
            "city-id": '330100',
            "device-id": '865223034945792',
            "site-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "app-visit-path": 'normal/bbs_home/bbs_strategy_column/bbs_strategy_detail',
            "client-id": '205',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "page-id": '47cb0a5a-1086-47e0-a10d-4ab2459f3e20',
            "app-id": '10000',
            "app-key": 'hunbasha_android',
            "view-id": 'a9b6a3c7-39d5-476f-917f-1c99f5243c8a',
            "app-channel": 'hunbohui',
            "app-version": '6.1.0',
            "Content-Type": 'application/json; charset=UTF-8',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip',
            "Connection": 'keep-alive',
            "Authorization": 'dmp ARRNOLiM9awOB1d5fCH9HVgaGjisjPWsDANUYnwu4R9LBhZn/oLt+lRZA253KfoeSgYBYOyb/KIfXAQkEnGrD0AUCmXqn/25BA1EMWss/kkbBl1k7pj6vFgMX3h0ff8UHAMLabrP/eoPUlQpLw=='
        }
        return response(json=json, headers=headers)

    @request(url='zone/reply/post-collect', method='post')
    def post_zone_reply_collect(self, type, reply_id):
        """
        第一个攻略页面，对第一个评论进行收藏
        """

        json = {
            "type": type,
            "reply_id": reply_id
        }
        headers = {
            "city-id": '330100',
            "device-id": '865223034945792',
            "site-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "app-visit-path": 'normal/bbs_home/bbs_strategy_column/bbs_strategy_detail/answer_detail',
            "client-id": '205',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "page-id": '47cb0a5a-1086-47e0-a10d-4ab2459f3e20',
            "app-id": '10000',
            "app-key": 'hunbasha_android',
            "view-id": 'a9b6a3c7-39d5-476f-917f-1c99f5243c8a',
            "app-channel": 'hunbohui',
            "app-version": '6.1.0',
            "Content-Type": 'application/json; charset=UTF-8',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip',
            "Connection": 'keep-alive',
            "Authorization": 'dmp ARRNOLiM9awOB1d5fCH9HVgaGjisjPWsDANUYnwu4R9LBhZn/oLt+lRZA253KfoeSgYBYOyb/KIfXAQkEnGrD0AUCmXqn/25BA1EMWss/kkbBl1k7pj6vFgMX3h0ff8UHAMLabrP/eoPUlQpLw=='
        }
        return response(json=json, headers=headers)

    @request(url='zone/reply/post-comment', method='post')
    def post_zone_reply_comment(self, content, reply_id, reply_topid):
        """
        第一个攻略页面，对第一个评论进行回复
        """

        json = {
            "content": content,
            "reply_id": reply_id,
            "reply_topid":reply_topid
        }
        headers = {
            "city-id": '330100',
            "device-id": '865223034945792',
            "site-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "app-visit-path": 'normal/bbs_home/bbs_strategy_column/bbs_strategy_detail/answer_detail',
            "client-id": '205',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "page-id": '47cb0a5a-1086-47e0-a10d-4ab2459f3e20',
            "app-id": '10000',
            "app-key": 'hunbasha_android',
            "view-id": 'a9b6a3c7-39d5-476f-917f-1c99f5243c8a',
            "app-channel": 'hunbohui',
            "app-version": '6.1.0',
            "Content-Type": 'application/json; charset=UTF-8',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip',
            "Connection": 'keep-alive',
            "Authorization": 'dmp ARRNOLiM9awOB1d5fCH9HVgaGjisjPWsDANUYnwu4R9LBhZn/oLt+lRZA253KfoeSgYBYOyb/KIfXAQkEnGrD0AUCmXqn/25BA1EMWss/kkbBl1k7pj6vFgMX3h0ff8UHAMLabrP/eoPUlQpLw=='
        }
        return response(json=json, headers=headers)

    @request(url='zone/reply/delete-reply', method='post')
    def delete_zone_reply(self, reply_id, reply_topid):
        """
        第一个攻略页面，对第一个评论的回复，将回复删除
        """

        json = {
            "reply_id": reply_id,
            "reply_topid": reply_topid
        }
        headers = {
            "city-id": '330100',
            "device-id": '865223034945792',
            "site-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "app-visit-path": 'normal/bbs_home/bbs_strategy_column/bbs_strategy_detail/answer_detail',
            "client-id": '205',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "page-id": '47cb0a5a-1086-47e0-a10d-4ab2459f3e20',
            "app-id": '10000',
            "app-key": 'hunbasha_android',
            "view-id": 'a9b6a3c7-39d5-476f-917f-1c99f5243c8a',
            "app-channel": 'hunbohui',
            "app-version": '6.1.0',
            "Content-Type": 'application/json; charset=UTF-8',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip',
            "Connection": 'keep-alive',
            "Authorization": 'dmp ARRNOLiM9awOB1d5fCH9HVgaGjisjPWsDANUYnwu4R9LBhZn/oLt+lRZA253KfoeSgYBYOyb/KIfXAQkEnGrD0AUCmXqn/25BA1EMWss/kkbBl1k7pj6vFgMX3h0ff8UHAMLabrP/eoPUlQpLw=='
        }
        return response(json=json, headers=headers)

    @request(url='zone/home/get-search', method='post')
    def get_zone_home_search(self, pageNum, type, keyword):
        """
        "结婚攻略"页面，顶部搜索
        """

        json = {
            "pageNum": pageNum,
            "type": type,
            "keyword": keyword
        }
        headers = {
            "city-id": '330100',
            "device-id": '865223034945792',
            "site-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "app-visit-path": 'normal/bbs_home/bbs_search/bbs_search_result',
            "client-id": '205',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "page-id": '47cb0a5a-1086-47e0-a10d-4ab2459f3e20',
            "app-id": '10000',
            "app-key": 'hunbasha_android',
            "view-id": 'a9b6a3c7-39d5-476f-917f-1c99f5243c8a',
            "app-channel": 'hunbohui',
            "app-version": '6.1.0',
            "Content-Type": 'application/json; charset=UTF-8',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip',
            "Connection": 'keep-alive',
            "Authorization": 'dmp ARRNOLiM9awOB1d5fCH9HVgaGjisjPWsDANUYnwu4R9LBhZn/oLt+lRZA253KfoeSgYBYOyb/KIfXAQkEnGrD0AUCmXqn/25BA1EMWss/kkbBl1k7pj6vFgMX3h0ff8UHAMLabrP/eoPUlQpLw=='
        }
        return response(json=json, headers=headers)

    @request(url='commact/get-my-activity', method='post')
    def get_my_activity(self, pageNum, pageSize):
        """
        查看我的活动
        """

        json = {
            "pageNum": pageNum,
            "pageSize": pageSize
        }
        headers = {
            "city-id": '330100',
            "device-id": '865223034945792',
            "site-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "app-visit-path": 'normal/mine/my_activity_list',
            "client-id": '205',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36',
            "visit-city-name": '%E6%9D%AD%E5%B7%9E%E5%B8%82',
            "page-id": '47cb0a5a-1086-47e0-a10d-4ab2459f3e20',
            "app-id": '10000',
            "app-key": 'hunbasha_android',
            "view-id": 'a9b6a3c7-39d5-476f-917f-1c99f5243c8a',
            "app-channel": 'hunbohui',
            "app-version": '6.1.0',
            "Content-Type": 'application/json; charset=UTF-8',
            "Host": 'open.test.jiehun.com.cn',
            "Accept-Encoding": 'gzip',
            "Connection": 'keep-alive',
            "Authorization": 'dmp ARRNOLiM9awOB1d5fCH9HVgaGjisjPWsDANUYnwu4R9LBhZn/oLt+lRZA253KfoeSQ4OaOqb96IfXAQkEnGrD0AUCmXqn/25BA1EMWt6rh1OBQE06Mr4vAwEUS4rK6xIHAJdNOnP971YUAB8Kw=='
        }
        return response(json=json, headers=headers)

