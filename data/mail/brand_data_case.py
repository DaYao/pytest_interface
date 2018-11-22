# @Time    :2018/10/29 16:57
# @Author  :lvjunjie
from utils.cfg import CONFIG
from data import data_count

brand_count_add = data_count.DataAddCount().dmp_base_brand_data_count()
brand_count_get = data_count.DataGetCount().get_dmp_base_brand_data_count()

class BrandDataCase:

    def brand_list_data(self):
        return [
            {
                "username":CONFIG.ACCOUNT.CRM_USER[0],
                "password":CONFIG.ACCOUNT.CRM_USER[1],
                "assert_contents": ["<title>品牌列表</title>",
                                "品牌ID", "品牌名称", "英文名称", "品牌别名", "覆盖平台行业", "提交时间", "注册地",
                                "审核状态", "启用状态", "最后操作人", "操作"
                                ]
            },
            {
                "username": CONFIG.ACCOUNT.APP_USER[0],
                "password": CONFIG.ACCOUNT.APP_USER[1],
                "assert_contents": ["<title>品牌列表</title>",
                                "品牌ID", "品牌名称", "英文名称", "品牌别名", "覆盖平台行业", "提交时间", "注册地",
                                "审核状态", "启用状态", "最后操作人", "操作"
                                ]
            }
        ]

    def brand_select_data(self):
        return [
            {
                "username":CONFIG.ACCOUNT.CRM_USER[0],
                "password":CONFIG.ACCOUNT.CRM_USER[1],
                "assert_contents": ["<title>品牌列表</title>",
                                "品牌ID", "品牌名称", "英文名称", "品牌别名", "覆盖平台行业", "提交时间", "注册地",
                                "审核状态", "启用状态", "最后操作人", "操作"
                                ]
            }
        ]

    def brand_save_data(self):
        return [
            {
                "username": CONFIG.ACCOUNT.CRM_USER[0],
                "password": CONFIG.ACCOUNT.CRM_USER[1],
                "registerLocation": "中国大陆",
                "nameCn": "测试品牌名称" + str(brand_count_add),
                "nameEn": "test_name" + str(brand_count_get),
                "nameAlias": "测试品牌别名" + str(brand_count_get),
                "intro": "测试品牌介绍" + str(brand_count_get),
                "registerIndustry": "制造业",
                "trademarkNumber": 660123,
                "trademarkApplicant": "测试申请人" + str(brand_count_get),
                "trademarkType": 1,
                "logo": "https://img.tthunbohui.cn/dmp/h/brand/1540915200/jh-img-orig-ga_1057445424459481088_794_605_206393.png",
                "trademarkCertificate": "https://img.tthunbohui.cn/dmp/h/brand/1540915200/jh-img-orig-ga_1057445434530004992_626_377_104473.png",
                "firstIndustryId": 0,
                "secondIndustryId": 0,
                "coverageIndustry": "4-2273"
            }
        ]

