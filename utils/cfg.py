# @Time    :2018/10/29 16:57
# @Author  :lvjunjie
import allure
import os


class Test:
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

    #MDP
    MDP_BASE_URL = "http://mdp.test.zghbh.com/v2"

    class ACCOUNT:
        DMP_TOP = '18111511257', '123456'
        APP_USER = '15757166394', 'ty123456'
        CRM_USER = '18000000000', '123456'
        User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'


class Online:

    # 婚博会APP    url  http
    HUNBOHUI_BASE_URL_HTTP = 'http://open.jiehun.com.cn'

    # 婚博会APP    url  https
    HUNBOHUI_BASE_URL_HTTPS = 'https://open.jiehun.com.cn'

    # 运营后台DMP   url
    SSOHUNBOHUI_BASE_URL = 'http://sso.tthunbohui.com'

    BOPSHUNBOHUI_BASE_URL = 'http://bops.tthunbohui.com'

    # CRM后台地址
    CRM_BASE_URL = 'http://crm.tthunbohui.com/'

    # CRM后台api地址
    CRM_BASE_URL_HTTP = 'http://crmapi.tthunbohui.com/'

    # hunbbohui db，dmp_message库
    HUNBOHUI_DATABASE = 'mysql+pymysql://root@test.dmp.mysqlm.jhops.club:3309/dmp_message?charset=utf8'


    class ACCOUNT:
        DMP_TOP = '18111511257', '123456'
        APP_USER = '15757166394', 'ty123456'
        CRM_USER = '18000000000', '123456'
        User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'


CONFIG = Test

BUILD_USER = os.getenv('BUILD_USER', 'tester')
if BUILD_USER == '':
    BUILD_USER = 'tester'

environment = os.getenv('environment', 'test')

if environment == 'test':
    CONFIG = Test
else:
    CONFIG = Test

# allure.environment(测试环境=environment, host=CONFIG.HUNBOHUI_BASE_URL_HTTP, 执行人=BUILD_USER, 测试项目='DMP后台接口')
