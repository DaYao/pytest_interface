# @Time    :2018/10/29 16:57
# @Author  :lvjunjie
import pytest
from apis.hbh_dmp_brand_api import DmpBrand
from data.mail.brand_data_case import BrandDataCase

brand_list_data = BrandDataCase().brand_list_data()
brand_select_data = BrandDataCase().brand_select_data()
brand_sava_data = BrandDataCase().brand_save_data()


class TestDmpBrand:

    @pytest.mark.parametrize('data', brand_list_data)
    def test_dmp_brand_list(self, data):
        """
        商城—品牌管理—品牌列表
        """
        dmp_brand = DmpBrand()
        dmp_brand.login_dmp(username=data['username'], password=data['password'])
        res = dmp_brand.dmp_base_brand_list()
        res_content = res.text
        assert res.status_code == 200 and res.elapsed.seconds <= 3
        for assert_text in data["assert_contents"]:
            assert assert_text in res_content

    @pytest.mark.parametrize('data', brand_select_data)
    def test_dmp_brand_select(self, data):
        """
        商城——品牌管理——品牌列表——品牌搜索
        """
        dmp_brand = DmpBrand()
        dmp_brand.login_dmp(username=data['username'], password=data['password'])
        res = dmp_brand.dmp_base_brand_select()
        res_json = res.json
        assert res.status_code == 200 and res.elapsed.seconds <= 3 and res_json['code'] == 0, "品牌搜索接口断言"

    @pytest.mark.parametrize('data', brand_sava_data)
    def test_dmp_brand_sava(self, data):
        """
        1.新增品牌
        2.品牌搜索
        3.删除品牌
        4.品牌搜索
        """
        dmp_brand = DmpBrand()
        dmp_brand.login_dmp(username=data['username'], password=data['password'])

        res = dmp_brand.dmp_base_brand_save(registerLocation=data["registerLocation"], nameCn=data["nameCn"],
                                            nameEn=data["nameEn"], nameAlias=data["nameAlias"], intro=data["intro"],
                                            registerIndustry=data["registerIndustry"], trademarkNumber=data["trademarkNumber"],
                                            trademarkApplicant=data["trademarkApplicant"],  trademarkType=data["trademarkType"], logo=data["logo"],
                                            trademarkCertificate=data["trademarkCertificate"],  firstIndustryId=data["firstIndustryId"],
                                            secondIndustryId=data["secondIndustryId"], coverageIndustry=data["coverageIndustry"])
        res_json = res.json
        assert res.status_code == 200 and res.elapsed.seconds <= 3 and res_json['code'] == 0

        res = dmp_brand.dmp_base_brand_select(brandName=data["nameCn"])
        res_json = res.json
        assert res.status_code == 200 and res.elapsed.seconds <= 3 and res_json['code'] == 0
        res_data = res_json['data']['list'][0]
        assert res_data['nameCn'] == data["nameCn"] and res_data['nameEn'] == data["nameEn"] and \
               res_data['nameAlias'] == data['nameAlias']
        brandId = res_data['brandId']
        print(brandId)
        res = dmp_brand.dmp_brand_remove(brandId=brandId)
        res_json = res.json
        assert res.status_code == 200 and res.elapsed.seconds <= 3 and res_json['code'] == 0 and res_json['data'] == "删除成功"
        res = dmp_brand.dmp_base_brand_select(brandName=data["nameCn"])
        res_json = res.json
        assert res.status_code == 200 and res.elapsed.seconds <= 3 and res_json['code'] == 0
        assert not res_json['data']['list']
