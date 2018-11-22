# coding=utf-8

import redis
import os
import allure

DATA_HOST = 'http://172.16.6.52/'

class TEST:
    # 婚博会APP    url  http
    HUNBOHUI_BASE_URL_HTTP = 'http://open.test.jiehun.com.cn'

    # 婚博会APP    url  https
    HUNBOHUI_BASE_URL_HTTPS = 'https://open.test.jiehun.com.cn'

    # 运营后台DMP   url
    SSOHUNBOHUI_BASE_URL = 'http://sso.test.tthunbohui.com'

    BOPSHUNBOHUI_BASE_URL = 'http://bops.test.tthunbohui.com'

    # CRM后台地址
    CRM_BASE_URL = 'http://crm.test.tthunbohui.com/'

    # CRM后台api地址
    CRM_BASE_URL_HTTP = 'http://crmapi.test.tthunbohui.com/'

    # hunbbohui db，dmp_message库
    HUNBOHUI_DATABASE = 'mysql+pymysql://root@test.dmp.mysqlm.jhops.club:3309/dmp_message?charset=utf8'

    class ACCOUNT:
        DMP_TOP = '18111511257', '123456'
        APP_USER = '15757166394', 'ty123456'
        CRM_USER = '18000000000', '123456'


class BETA:
    # 婚博会APP    url  http
    HUNBOHUI_BASE_URL_HTTP = 'http://open.test.jiehun.com.cn'

    # 婚博会APP    url  https
    HUNBOHUI_BASE_URL_HTTPS = 'https://open.test.jiehun.com.cn'

    # 运营后台DMP   url
    SSOHUNBOHUI_BASE_URL = 'http://sso.test.tthunbohui.com'

    BOPSHUNBOHUI_BASE_URL = 'http://bops.test.tthunbohui.com'

    # CRM后台地址
    CRM_BASE_URL = 'http://crm.test.tthunbohui.com/'

    # CRM后台api地址
    CRM_BASE_URL_HTTP = 'http://crmapi.test.tthunbohui.com/'

    # hunbbohui db，dmp_message库
    HUNBOHUI_DATABASE = 'mysql+pymysql://root@test.dmp.mysqlm.jhops.club:3309/dmp_message?charset=utf8'

    class ACCOUNT:
        DMP_TOP = '18111511257', '123456'
        APP_USER = '15757166394', 'ty123456'
        CRM_USER = '18000000000', '123456'

BUILD_USER = os.getenv('BUILD_USER', 'tester')
if BUILD_USER == '':
    BUILD_USER = 'tester'
environment = os.getenv('environment', 'qafc')

if environment == 'test':
    CONFIG = TEST
elif environment == 'beta':
    CONFIG = BETA
else:
    CONFIG = TEST

allure.environment(测试环境=environment, host=CONFIG.XG_GARDEN_BASE_URL, 执行人=BUILD_USER)
