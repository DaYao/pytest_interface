# @Time    :2018/10/29 16:57
# @Author  :lvjunjie
from common.api import request
from utils.cfg import CONFIG
from apis.hbh_dmp_login_api import LoginApi

host = CONFIG.BOPSHUNBOHUI_BASE_URL


class DmpBrand:

    def __init__(self):
        self.base_url = host
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }

    def login_dmp(self, username, password):
        dmp_login = LoginApi()
        res = dmp_login.logindmp(username=username, password=password)[0]
        Cookie = res.request.headers['Cookie']
        self.headers["Cookie"] = Cookie

    @request(url='/base/brand/list', method='get')
    def dmp_base_brand_list(self):
        """
        品牌列表接口
        """
        return {"headers": self.headers}

    @request(url='/base/industry/listsecondbyfirst', method='get')
    def dmp_base_industry_listsecondbyfirst(self, industryCateId=4):
        """
        通过一级行业查找对应的二级行业
        :param industryCateId:一级行业id
        :return:
        """
        params = {
            "industryCateId": industryCateId
        }
        return {"params": params}

    @request(url='/base/brand/select', method='get')
    def dmp_base_brand_select(self, pageNum=1, pageSize=20, brandId='', brandName='', firstIndustryCateId=0,
                              secondIndustryCateId=0, registerLocation='', isVerified='', isUse='', startTime='',
                              endTime=''):
        """
        品牌搜索
        :param pageNum:页码
        :param pageSize:每页显示条数
        :param brandId:品牌ID
        :param brandName:品牌名称
        :param firstIndustryCateId:一级行业
        :param secondIndustryCateId:二级行业
        :param registerLocation:注册地
        :param isVerified:审核状态
        :param isUse:启用/禁用
        :param startTime:提交时间(开始)
        :param endTime:提交时间(结束)
        :return:{"code": 0, "message": "成功", "data": null, "serviceTime": 1540799924, "success": true }
        """
        params = {
            "pageNum": pageNum,
            "pageSize": pageSize,
            "brandId": brandId,
            "brandName": brandName,
            "firstIndustryCateId": firstIndustryCateId,
            "secondIndustryCateId": secondIndustryCateId,
            "registerLocation": registerLocation,
            "isVerified": isVerified,
            "isUse": isUse,
            "startTime": startTime,
            "endTime": endTime
        }
        return {"params": params}

    @request(url='/base/brand/save', method='post')
    def dmp_base_brand_save(self, registerLocation=None, nameCn=None, nameEn=None, nameAlias=None, intro=None,
                            registerIndustry=None, trademarkNumber=None, trademarkApplicant=None, trademarkType=None,
                            logo=None, trademarkCertificate=None, firstIndustryId=None, secondIndustryId=None,
                            coverageIndustry=None):
        """
        添加品牌
        :param registerLocation:注册地
        :param nameCn: 品牌名称
        :param nameEn:品牌英文名称
        :param nameAlias:品牌別名
        :param intro:品牌介绍
        :param registerIndustry:品牌注册所属行业
        :param trademarkNumber:商标申请号
        :param trademarkApplicant:商标申请人
        :param trademarkType:注册类型
        :param logo:品牌logo
        :param trademarkCertificate:商标注册证/受理通知书
        :param firstIndustryId:第一产业ID
        :param secondIndustryId:第二产业ID
        :param coverageIndustry:覆盖产业
        :return:
        """
        data = {
            "registerLocation": registerLocation,
            "nameCn": nameCn,
            "nameEn": nameEn,
            "nameAlias": nameAlias,
            "intro": intro,
            "registerIndustry": registerIndustry,
            "trademarkNumber": trademarkNumber,
            "trademarkApplicant": trademarkApplicant,
            "trademarkType": trademarkType,
            "logo": logo,
            "trademarkCertificate": trademarkCertificate,
            "firstIndustryId": firstIndustryId,
            "secondIndustryId": secondIndustryId,
            "coverageIndustry": coverageIndustry
        }
        return {"data": data}

    @request(url='/base/brand/remove', method='get')
    def dmp_brand_remove(self, brandId):
        """
        删除品牌接口
        :param brandId: 品牌ID
        :return:{"code": 0, "message": "成功", "data": "删除成功", "serviceTime": 1540976751, "success": true }
        """
        params = {
            "brandId": brandId
        }
        return {"params": params}


# if __name__ == '__main__':
#     dmp_brand = DmpBrand()
#     dmp_brand.login_dmp('18000000000','123456')
#     res = dmp_brand.dmp_base_brand_list()
#     res = res.content
