# coding=utf-8
from urllib.parse import unquote
from pithy import request, response, make_session
from utils.cfg import CONFIG
from .sso import SSO
from requests.utils import dict_from_cookiejar


class HunbohuiCrmApi(object):
    def __init__(self):
        self.base_url = CONFIG.CRM_BASE_URL_HTTP
        self.sso_api = SSO()
        self.session = make_session()

    @request(url=CONFIG.CRM_BASE_URL, method='get')
    def _login(self, login_name, password):
        """
        sso登录获取session信息
        """
        res = self.sso_api.sso_login(login_name, password)
        res.content
        self.session = res.session
        return response()

    def login(self, login_name, password):
        """
        CRM登录
        """
        res = self._login(login_name, password)
        dict_cookies = dict_from_cookiejar(res.cookies)
        self.session.headers['Authorization'] = unquote(dict_cookies['user_session'])
        self.session = res.session



    @request(url='/crm/authcode/getemailcode', method='get')
    def getemailcode(self):
        """
        获取邮箱验证码
        """

        _json = "string"
        return response(json=_json)

    @request(method='get')
    def getphonecode(self, phone):
        """
        获取手机验证码
        """

        url = '/crm/authcode/getphonecode?phone={}'.format(phone)
        return response(url=url)

    @request(url='/crm/authority/managegroup/edit', method='post')
    def managegroupedit(self, manageGroupName, mgid, parentId, webSiteTypeList):
        """
        添加/编辑管理组
        """

        _json = {
            "manageGroupName": manageGroupName,
            "mgid": mgid,
            "parentId": parentId,
            "webSiteTypeList":
                webSiteTypeList

        }
        return response(json=_json)

    @request(url='/crm/authority/managegroup/listbylevel', method='get')
    def listbylevel(self):
        """
        获得对应级别的所有组
        """

        _json = 1
        return response(json=_json)

    @request(url='/crm/authority/managegroup/listwithlevel', method='get')
    def listwithlevel(self):
        """
        获取所有级别的管理组(分级)
        """

        return response()

    @request(url='/crm/authority/managegroup/member/list', method='get')
    def managegroupmemberlist(self, mgid):
        """
        获得该管理组下的所有成员
        """

        params = {
            "mgid": mgid
        }
        return response(params=params)

    @request(url='/crm/authority/managegroup/member/updatetype', method='post')
    def managegroupmemberupdatetype(self, prpid, role):
        """
        更改该成员的组内身份
        """

        _json = {
            "prpid": prpid,
            "role": role
        }
        return response(json=_json)

    @request(url='/crm/authority/managegroup/permission/edit', method='post')
    def permissionedit(self, mgid, pupidList):
        """
        为管理组分配权限
        """

        _json = {
            "mgid": mgid,
            "pupidList": pupidList
        }
        return response(json=_json)

    @request(url='/crm/authority/managegroup/permission/showandedit', method='get')
    def permissionshowandedit(self, mgid):
        """
        显示管理组分配权限页面
        """

        params = {
            "mgid": mgid
        }
        return response(params=params)

    @request(url='/crm/authority/managegroup/permission/website/list', method='get')
    def list(self):
        """
        返回设置菜单权限网址列表页面
        """

        params = {
            "pageNum": 1,
            "pageSize": 1
        }
        _json = 1
        return response(params=params, json=_json)

    @request(url='/crm/authority/managegroup/permission/website/operate', method='get')
    def operate(self):
        """
        管理组下权限网址列表启用禁用操作
        """

        params = {
            "isUse": 1
        }
        _json = 1
        return response(params=params, json=_json)

    @request(url='/crm/authority/managegroup/permission/website/synchronization', method='get')
    def synchronization(self):
        """
        同步数据操作
        """

        return response()

    @request(url='/crm/authority/managegroup/remove', method='get')
    def remove(self):
        """
        根据管理组id删除对应的管理组
        """

        params = {
            "mgid": 1
        }
        return response(params=params)

    @request(url='/crm/authority/managegroup/show/getbypuid', method='get')
    def getbypuid(self):
        """
        管理员编辑所属组时数据管理组数据回显
        """

        params = {
            "puid": 1
        }
        return response(params=params)

    @request(url='/crm/authority/managegroup/show/listbyparentid', method='get')
    def listbyparentid(self, parentId):
        """
        根据父级管理组id获得所有子级管理组集合
        """

        params = {
            "parentId": parentId
        }
        return response(params=params)

    @request(url='/crm/authority/managegroup/showedit', method='get')
    def managegroupshowedit(self, mgid):
        """
        显示管理组编辑页面
        """

        params = {
            "mgid": mgid
        }
        return response(params=params)

    @request(url='/crm/authority/managegroup/websitetype/listwebsitetypebymanagegroupparentid', method='get')
    def listwebsitetypebymanagegroupparentid(self):
        """
        根据管理组id获得其子级组可以选择的网址类型
        """

        _json = 1
        return response(json=_json)

    @request(url='/crm/authority/permission/edit', method='post')
    def edit(self):
        """
        添加编辑权限列表（菜单）
        """

        _json = {
            "parentId": 1,
            "pupid": 1,
            "puserPermissionName": "string",
            "type": 1,
            "url": "string"
        }
        return response(json=_json)

    @request(url='/crm/authority/permission/list', method='get')
    def list(self):
        """
        查询所有管理员的一级权限列表
        """

        return response()

    @request(url='/crm/authority/permission/listpermissionbypuser', method='get')
    def listpermissionbypuser(self):
        """
        获取登录管理员权限列表
        """

        return response()

    @request(url='/crm/authority/permission/liststchild', method='get')
    def liststchild(self):
        """
        根据一级权限id获得所有二三级权限json数据
        """

        params = {
            "pupid": 1
        }
        return response(params=params)

    @request(method='get')
    def deletepuser(self, puid):
        """
        删除管理员
        """

        url = '/crm/authority/puser/del?puid={}'.format(puid)
        return response(url=url)

    @request(url='/crm/authority/puser/get', method='get')
    def authoritypuserget(self):
        """
        获取登录管理员信息
        """

        return response()

    @request(url='/crm/authority/puser/group/edit', method='post')
    def puseredit(self):
        """
        编辑管理员的所属组提交
        """

        _json = {
            "choiceCitySite": [
                1
            ],
            "firstGroup": 1,
            "puid": 1,
            "secondGroup": 1,
            "thirdGroup": 1
        }
        return response(json=_json)

    @request(url='/crm/authority/puser/group/editshow', method='get')
    def pusereditshow(self):
        """
        编辑管理员的所属组数据回显
        """

        params = {
            "puid": 1
        }
        return response(params=params)

    @request(url='/crm/authority/puser/list', method='post')
    def puserlist(self, mobile, realname):
        """
        根据手机号和真实姓名查询管理员列表
        """

        _json = {
            "mobile": mobile,
            "pageNum": 1,
            "pageSize": 20,
            "realname": realname
        }
        return response(json=_json)

    @request(method='get')
    def puserpermissionlist(self, puid):
        """
        查看管理员权限
        """

        url = '/crm/authority/puser/permission/list?puid={}'.format(puid)
        return response(url=url)

    @request(url='/crm/authority/puser/savepuser', method='post')
    def savepuser(self, mobile, realname):
        """
        添加管理员
        """

        _json = {
            "mobile": mobile,
            "realname": realname
        }
        return response(json=_json)

    @request(url='/crm/authority/puser/update', method='post')
    def authoritypuserupdate(self, mobile, personalDeclaration, position):
        """
        更新登录管理员信息
        """

        _json = {
            "cityId": "110900",
            # "createdAt": "string",
            # "createdBy": 1,
            # "createdByName": "string",
            "departmentId": 1,
            # "departmentName": "string",
            # "memberId": 1,
            "mobile": mobile,
            # "newPwd": "string",
            # "oldPwd": "string",
            "personalDeclaration": personalDeclaration,
            # "personalImg": "string",
            "position": position,
            # "puid": 1,
            # "realName": "string",
            # "updatedAt": "string",
            # "updatedBy": 1,
            # "updatedByName": "string"
        }
        return response(json=_json)

    @request(url='/crm/authority/puser/updaterealname', method='post')
    def updaterealname(self, puid, realname):
        """
        更新指定管理员名字
        """

        _json = {
            "puid": puid,
            "realname": realname
        }
        return response(json=_json)

    @request(url='/crm/authority/puserpermissionwebsite/listbypupid', method='get')
    def listbypupid(self, pupid):
        """
        根据管理员权限id获得该权限对应的网址列表 页面
        """

        params = {
            "pupid": pupid
        }
        return response(params=params)

    @request(url='/crm/authority/puserpermissionwebsite/remove', method='get')
    def remove(self, ppwid):
        """
        根据权限和网址中间表的id 进行删除操作
        """

        params = {
            "ppwid": ppwid
        }
        return response(params=params)

    @request(url='/crm/authority/puserpermissionwebsite/save', method='post')
    def save(self, pupid, wsidList):
        """
        添加权限和网址之间的关联
        """

        _json = {
            "pupid": pupid,
            "wsidList": [
                wsidList
            ]
        }
        return response(json=_json)

    @request(url='/crm/authority/website/add', method='post')
    def websiteadd(self, isRelationCitySite, type, url, websiteName):
        """
        添加新的网址
        """

        _json = {
            # "createdAt": "string",
            # "createdBy": 1,
            # "delFlag": 1,
            # "id": 1,
            # "idStr": "string",
            "isRelationCitySite": isRelationCitySite,
            # "isUse": 1,
            "type": type,
            # "updatedAt": "string",
            # "updatedBy": 1,
            "url": url,
            "websiteName": websiteName
            # "wsid": 1
        }
        return response(json=_json)

    @request(url='/crm/authority/website/get', method='get')
    def websiteget(self, wsid):
        """
        根据网址id获得网址实体实现数据回显
        """

        params = {
            "wsid": wsid
        }
        return response(params=params)

    @request(url='/crm/authority/website/list', method='post')
    def websitelist(self, websiteName):
        """
        获得所有的网址列表页面
        """

        _json = {
            "pageNum": 1,
            "pageSize": 20,
            "url": "",
            "websiteName": websiteName
        }
        return response(json=_json)

    @request(method='get')
    def websiteoperate(self, wsid, isuse):
        """
        启用禁用网址
        """

        url = '/crm/authority/website/operate?wsid={}&isuse={}'.format(wsid, isuse)

        return response(url=url)

    @request(method='get')
    def websiteremove(self, wsid):
        """
        删除网址
        """

        url = '/crm/authority/website/remove?wsid={}'.format(wsid)

        return response(url=url)

    @request(url='/crm/authority/website/select', method='post')
    def websiteselect(self, url, websiteName):
        """
        搜索网址
        """

        _json = {
            "pageNum": 1,
            "pageSize": 20,
            "url": url,
            "websiteName": websiteName
        }
        return response(json=_json)

    @request(url='/crm/authority/website/selectbyname', method='get')
    def websiteselectbyname(self, webSiteName):
        """
        根据网址名称进行模糊查询
        """

        params = {
            "webSiteName": webSiteName
        }
        return response(params=params)

    @request(url='/crm/department/getbyid', method='get')
    def departmentgetbyid(self, id):
        """
        根据ID查询部门信息
        """

        params = {
            "id": id
        }
        return response(params=params)

    @request(url='/crm/department/listbycityid', method='get')
    def listbycityid(self, cityId):
        """
        根据城市ID查询部门集合
        """

        params = {
            "cityId": cityId
        }
        return response(params=params)

    @request(url='/crm/imgcode/getimgcode', method='post')
    def getimgcode(self):
        """
        获取图片验证码
        """

        _json = {
            "email": "string",
            "phone": "string",
            "registerType": "string"
        }
        return response(json=_json)

    @request(url='/crm/member/addcompany', method='post')
    def addcompany(self, commercialImg, commercialNumber, companyName, memberId, personalCardImgA, personalCardImgB, personalId, realName):
        """
        企业资料入驻
        """

        _json = {
        "commercialImg": commercialImg,
        "commercialNumber": commercialNumber,
        "companyName": companyName,
        # "createdBy": 1,
        "memberId": memberId,
        "memberType": 2,
        "personalCardImgA": personalCardImgA,
        "personalCardImgB": personalCardImgB,
        "personalId": personalId,
        "realName": realName
        # "updatedBy": 1
        }
        return response(json=_json)

    @request(url='/crm/member/addcompanyverify', method='post')
    def memberaddcompanyverify(self, authCode):
        """
        CRM新增企业审核信息
        """

        _json = {
            "authCode": authCode,
            "cityId": 1,
            "createdBy": 1,
            "email": "string",
            "imgCode": "string",
            "memberActor": "string",
            "memberName": "string",
            "memberType": "string",
            "password": "string",
            "phone": "string",
            "updatedBy": 1
        }
        return response(json=_json)

    @request(url='/crm/member/addemail', method='post')
    def memberaddemail(self):
        """
        会员绑定邮箱
        """

        _json = {
            "authCode": "string",
            "createdBy": 1,
            "email": "string",
            "memberId": 1,
            "newAuthCode": "string",
            "newEmail": "string",
            "updatedBy": 1
        }
        return response(json=_json)

    @request(url='/crm/member/addmemberemail', method='post')
    def addmemberemail(self, email, memberName, password, phone):
        """
        CRM线上新增普通会员(邮箱)
        """

        _json = {
            "authCode": "888888",
            "cityId": 110900,
            # "createdBy": 1,
            "email": email,
            # "imgCode": "string",
            "memberActor": "10-10",
            "memberName": memberName,
            "memberType": 1,
            "password": password,
            "phone": phone,
            # "updatedBy": 1
        }
        return response(json=_json)

    @request(url='/crm/member/addmemberphone', method='post')
    def addmemberphone(self, authCode, memberName, password, phone):
        """
        CRM线上新增普通会员(手机)
        """

        _json = {
            "authCode": authCode,
            "cityId": 110900,
            # "createdBy": 1,
            # "email": "string",
            # "imgCode": "string",
            "memberActor": '10-10',
            "memberName": memberName,
            "memberType": 0,
            "password": password,
            "phone": phone
            # "updatedBy": 1
        }
        return response(json=_json)

    @request(url='/crm/member/addmemberphone', method='post')
    def addmemberphone1(self, authCode, memberName, password, phone):
        """
        CRM线上新增普通会员(手机)【企业会员注册】
        """

        _json = {
            "authCode": authCode,
            "cityId": 110900,
            # "createdBy": 1,
            # "email": "string",
            # "imgCode": "string",
            "memberActor": '10-10',
            "memberName": memberName,
            "memberType": 1,
            "password": password,
            "phone": phone
            # "updatedBy": 1
        }
        return response(json=_json)

    @request(url='/crm/member/commercialreturn', method='post')
    def commercialreturn(self, commercialReturnDesc, commercialVerifyState, memberId):
        """
        企业执照审核退回
        """

        _json = {
            # "businessScope": "string",
            # "commercialBeginAt": 1,
            # "commercialEndAt": 1,
            # "commercialImg": "string",
            # "commercialName": "string",
            # "commercialNumber": "string",
            "commercialReturnDesc": commercialReturnDesc,
            "commercialVerifyState": commercialVerifyState,
            # "companyName": "string",
            # "companyType": "string",
            # "createdBy": 1,
            # "domicile": "string",
            "memberId": memberId,
            # "memberType": "string",
            # "personalCardAddr": "string",
            # "personalCardExpire": "string",
            # "personalCardImgA": "string",
            # "personalCardImgB": "string",
            # "personalCardVerifyState": "string",
            # "personalId": "string",
            # "realName": "string",
            # "setUpDate": "string",
            # "updatedBy": 1
        }
        return response(json=_json)

    @request(url='/crm/member/commercialverify', method='post')
    def commercialverify(self, memberId, commercialVerifyState):
        """
        企业执照审核
        """

        _json = {
            # "businessScope": "string",
            # "commercialBeginAt": 1,
            # "commercialEndAt": 1,
            # "commercialImg": "string",
            # "commercialName": "string",
            # "commercialNumber": "string",
            # "commercialReturnDesc": "string",
            "commercialVerifyState": commercialVerifyState,
            # "companyName": "string",
            # "companyType": "string",
            # "createdBy": 1,
            # "domicile": "string",
            "memberId": memberId,
            # "memberType": "string",
            # "personalCardAddr": "string",
            # "personalCardExpire": "string",
            # "personalCardImgA": "string",
            # "personalCardImgB": "string",
            # "personalCardVerifyState": "string",
            # "personalId": "string",
            # "realName": "string",
            # "setUpDate": "string",
            # "updatedBy": 1
        }
        return response(json=_json)

    @request(url='/crm/member/companypersonalreturn', method='post')
    def companypersonalreturn(self, personalCardVerifyState, memberId, personalReturnDesc):
        """
        企业身份证审核退回
        """

        _json = {
            # "commercialVerifyState": "string",
            # "createdBy": 1,
            "memberId": memberId,
            # "personalCardAddr": "string",
            # "personalCardExpire": "string",
            "personalCardVerifyState": personalCardVerifyState,
            "personalReturnDesc": personalReturnDesc,
            # "updatedBy": 1
        }
        return response(json=_json)

    @request(url='/crm/member/companypersonalverify', method='post')
    def companypersonalverify(self, memberId, personalCardVerifyState):
        """
        企业身份证审核通过
        """

        _json = {
            "memberId": memberId,
            # "commercialVerifyState": "string",
            # "createdBy": 1,
            "personalCardAddr": "测试地址",
            # "personalCardExpire": "string",
            "personalCardVerifyState": personalCardVerifyState,
            "personalReturnDesc": "",
            # "updatedBy": 1
        }
        return response(json=_json)

    @request(url='/crm/member/convertcompanyenter', method='post')
    def convertcompanyenter(self, realName, commercialImg, commercialName, commercialNumber, memberId, memberType, personalCardImgA, personalCardImgB, personalId):
        """
        个人转为企业入驻
        """

        _json = {
            "realName": realName,
            # "businessScope": "string",
            # "commercialBeginAt": 1,
            # "commercialEndAt": 1,
            "commercialImg": commercialImg,
            "commercialName": commercialName,
            "commercialNumber": commercialNumber,
            # "commercialReturnDesc": "string",
            # "commercialVerifyState": "string",
            # "companyName": "string",
            # "companyType": "string",
            # "createdBy": 1,
            # "domicile": "string",
            "memberId": memberId,
            "memberType": memberType,
            # "personalCardAddr": "string",
            # "personalCardExpire": "string",
            "personalCardImgA": personalCardImgA,
            "personalCardImgB": personalCardImgB,
            # "personalCardVerifyState": "string",
            "personalId": personalId
            # "setUpDate": "string",
            # "updatedBy": 1
        }
        return response(json=_json)

    @request(url='/crm/member/generalverifyaccess', method='get')
    def generalverifyaccess(self, memberId, personalReturnDesc, addr, validityPeriod, personalCardVerifyState):
        """
        个人审核通过0723
        """

        url = '/crm/member/generalverifyaccess?memberId={}&personalReturnDesc={}&addr={}&validityPeriod={}&personalCardVerifyState={}'.format(memberId, personalReturnDesc, addr, validityPeriod, personalCardVerifyState)
        return response(url=url)

    @request(method='get')
    def generalverifyprocess(self, memberId, verifyState):
        """
        修改审核状态为审核中
        """

        url = '/crm/member/generalverifyprocess?memberId={}&verifyState={}'.format(memberId, verifyState)

        return response(url=url)

    @request(url='/crm/member/generalverifyreturn', method='post')
    def generalverifyreturn(self, memberId, personalCardVerifyState):
        """
        个人审核退回
        """

        _json = {

             "addr": "",
             # "createdBy": 0,
             "memberId": memberId,
             # "personalCardImgA": "string",
             # "personalCardImgB": "string",
             # "personalId": "string",
             "personalReturnDesc": "测试修改认证信息退回",
             "personalCardVerifyState": personalCardVerifyState,
             # "realName": "string",
             # "updatedBy": 0,
             "validityPeriod": ""
}
        return response(json=_json)

    @request(url='/crm/member/generalverifyupdate', method='post')
    def generalverifyupdate(self, addr, validityPeriod, realName, memberId, personalId):
        """
        个人认证信息修改
        """

        _json = {
            "addr": addr,
            "validityPeriod": validityPeriod,
            "realName": realName,
            "memberId": memberId,
            "personalId": personalId,
            "personalCardImgA": "https://img.tthunbohui.cn/dmp/s/merchant/1533139200/jh-img-orig-ga_1024905134288994304_373_228_13576.jpg",
            "personalCardImgB": "https://img.tthunbohui.cn/dmp/s/merchant/1533139200/jh-img-orig-ga_1024905141817769984_717_466_61102.jpg"
        }
        return response(json=_json)

    @request(method='get')
    def getmembercompanystore(self, memberId):
        """
        根据memberId获取企业会员店铺信息
        """

        url = '/crm/member/getmembercompanystore?memberId={}'.format(memberId)
        return response(url=url)

    @request(url='/crm/member/getmemberfull', method='post')
    def getmemberfull(self):
        """
        根据条件获取会员全部信息
        """

        _json = {
            "pageNum": 1,
            "pageSize": 20
        }
        return response(json=_json)

    @request(method='get')
    def getmemberfullcompany(self, memberId):
        """
        根据memberId获取企业会员全部信息
        """

        url = '/crm/member/getmemberfullcompany?memberId={}'.format(memberId)
        return response(url=url)

    @request(url='/crm/member/getmemberlist', method='post')
    def getmemberlist(self):
        """
        CRM根据条件获取会员(全部)
        """

        _json = {}
        return response(json=_json)

    @request(url='/crm/member/getmemberverify', method='post')
    def getmemberverify(self, verifyState):
        """
        根据条件获取会员审核信息
        """

        _json = {
            "verifyState": verifyState
        }
        return response(json=_json)

    @request(url='/crm/member/getverifyall', method='post')
    def getverifyall(self):
        """
        根据条件获取会员审核过程信息
        """

        _json = {}
        return response(json=_json)

    @request(url='/crm/member/modifylog/list', method='post')
    def membermodifyloglist(self):
        """
        查询修改记录列表
        """

        _json = {}
        return response(json=_json)

    @request(url='/crm/member/updatecommercialimg', method='post')
    def updatecommercialimg(self):
        """
        修改企业营业执照url
        """

        _json = {}
        return response(json=_json)

    @request(url='/crm/member/updatecompanyverify', method='post')
    def updatecompanyverify(self):
        """
        CRM修改企业会员认证信息
        """

        _json = {}
        return response(json=_json)

    @request(url='/crm/member/updatecompanyverifyinfo', method='post')
    def updatecompanyverifyinfo(self):
        """
        修改企业审核信息
        """

        _json = {}
        return response(json=_json)

    @request(url='/crm/member/updateemail', method='post')
    def updateemail(self):
        """
        会员修改邮箱
        """

        _json = {}
        return response(json=_json)

    @request(url='/crm/member/updatemember', method='post')
    def updatemember(self):
        """
        CRM线上修改会员
        """

        _json = {}
        return response(json=_json)

    @request(url='/crm/member/updatemembercompany', method='post')
    def updatemembercompany(self):
        """
        CRM修改企业会员信息
        """

        _json = {}
        return response(json=_json)

    @request(url='/crm/member/updatememberinfo', method='post')
    def updatememberinfo(self, memberId, memberName):
        """
        CRM修改会员基础信息
        """

        _json = {
            "addr": "测试地址",
            # "birthday": "2018-08-01T05:59:50.143Z",
            # "createdBy": 0,
            # "gender": "string",
            # "headPortrait": "string",
            "memberActor": "10-10",
            "memberId": memberId,
            "memberName": memberName
            # "updatedBy": 0,
            # "wedding": "2018-08-01T05:59:50.143Z"
        }
        return response(json=_json)

    @request(url='/crm/member/updatemembertype', method='post')
    def updatemembertype(self, memberId, memberType):
        """
        企业用户转普通会员用户
        """

        _json = {
            "memberId": memberId,
            "memberType": memberType
        }
        return response(json=_json)

    @request(url='/crm/member/updatememberverify', method='post')
    def updatememberverify(self):
        """
        CRM修改会员认证信息
        """

        _json = {}
        return response(json=_json)

    @request(url='/crm/member/updatepersonalimga', method='post')
    def updatepersonalimga(self):
        """
        修改企业上传身份图片A
        """

        _json = {}
        return response(json=_json)

    @request(url='/crm/member/updatepersonalimgb', method='post')
    def updatepersonalimgb(self):
        """
        修改企业上传身份图片B
        """

        _json = {}
        return response(json=_json)

    @request(url='/crm/member/updatephone', method='post')
    def updatephone(self, phone, authCode, memberId, newAuthCode, newPhone):
        """
        会员修改手机号
        """

        _json = {
               "phone": phone,
                "authCode": authCode,
                "memberId": memberId,
                "newAuthCode": newAuthCode,
                "newPhone": newPhone
                # "createdBy": 0,
                # "updatedBy": 0
        }
        return response(json=_json)

    @request(url='/crm/member/verifypersonalcard', method='post')
    def verifypersonalcard(self):
        """
        验证身份证的状态(不调用未实现)
        """

        params = {
            "personalCard": "string",
            "realName": "string"
        }
        return response(params=params)

    @request(method='get')
    def verifyprocess(self, memberId, verifyState):
        """
        企业审核中
        """

        url = '/crm/member/verifyprocess?memberId={}&verifyState={}'.format(memberId, verifyState)

        return response(url=url)

    @request(url='/crm/prodrole/addproduct', method='post')
    def prodroleaddproduct(self, productName, productDesc):
        """
        新增产品
        """

        javaScript= {
            "productName": productName,
            "productDesc": productDesc
        }
        return response(json=javaScript)

    @request(url='/crm/prodrole/addrole', method='post')
    def prodroleaddrole(self, roleName, roleDesc):
        """
        新增角色
        """

        _json = {
            "roleName": roleName,
            "roleDesc":roleDesc
        }
        return response(json=_json)

    @request(url='/crm/prodrole/handle', method='post')
    def prodrolehandle(self, op, type, id):
        """
        处理产品或角色
        """

        _json = {
        "op": op,
        "type": type,
        "id": id
        }
        return response(json=_json)

    @request(url='/crm/prodrole/list', method='get')
    def prodrolelist(self):
        """
        查询产品和角色列表
        """

        return response()

    @request(url='/crm/prodrole/listbyjoin', method='get')
    def prodrolelistbyjoin(self):
        """
        查询产品角色拼接列表
        """

        return response()

    @request(method='get')
    def prodrolelistbystate(self, state):
        """
        根据状态查询产品角色列表
        """

        url = '/crm/prodrole/listbystate?state={}'.format(state)

        return response(url=url)

    @request(url='/crm/sysmsg/listmsg', method='get')
    def sysmsglistmsg(self, state, pageNum, pageSize):
        """
        查看消息列表
        """

        params = {
            "state": state,
            "pageNum": pageNum,
            "pageSize": pageSize
        }
        return response(params=params)

    @request(url='/crm/sysmsg/readall', method='get')
    def sysmsgreadall(self):
        """
        全部设为已读
        """

        return response()

    @request(url='/crm/tag/add', method='post')
    def addtag(self, reason, tagName):
        """
        新增标签
        """

        _json = {
        "fatherTagId": 15,     #15代表轻奢
        "reason": reason,
        "tagName": tagName
        }
        return response(json=_json)

    @request(url='/crm/tag/get-record', method='post')
    def gettagrecord(self, status):
        """
        获取标签审核页
        """

        _json = {
            "pageNum": "0",
            "pageSize": "0",
            "status": status
        }
        return response(json=_json)

    @request(url='/crm/tag/get-tag-by-father', method='post')
    def gettagbyfather(self):
        """
        根据父级获取标签
        """

        _json = {
            "fatherTagId": 0
        }
        return response(json=_json)

    @request(url='/crm/tag/get-tag-by-level', method='post')
    def gettagbylevel(self):
        """
        根据层级获取标签
        """

        _json = {
            "level": 0
        }
        return response(json=_json)

    @request(url='/crm/tag/get-value', method='post')
    def getvalue(self, hbhId, tagId):
        """
        根据hbhId、tagId获取子标签数值
        """

        _json = {
           "hbhId": hbhId,
           "tagId": tagId
        }
        return response(json=_json)

    @request(url='/crm/tag/search', method='post')
    def searchtag(self):
        """
        查询标签
        """

        _json = {
        "pageNum": 1,
        "pageSize": 10,
        "tagId": 0,
        "tagName": ""
        }
        return response(json=_json)

    @request(url='/crm/tag/verify', method='post')
    def tagverify(self, crmTagRecordId, verify):
        """
        审核标签
        """

        _json = {
            # "createdBy": 0,
            # "updatedBy": 0,
            "crmTagRecordId": crmTagRecordId,
            "verify": verify
        }
        return response(json=_json)

    @request(url='/crm/view/add-view-class', method='post')
    def addviewclass(self, className):
        """
        创建分类
        """

        _json = {
            "className": className
        }
        return response(json=_json)

    @request(url='/crm/view/add-view-group', method='post')
    def add_view_group(self):
        """
        创建分组
        """

        _json = {}
        return response(json=_json)

    @request(url='/crm/view/get-users', method='post')
    def getusers(self, crmViewGroupId ):
        """
        获取分组会员
        """

        _json = {
            "crmViewGroupId": crmViewGroupId
        }
        return response(json=_json)

    @request(url='/crm/view/get-view-class', method='post')
    def getviewclass(self):
        """
        获取分类
        """

        return response()

    @request(url='/crm/view/get-view-group', method='post')
    def get_view_group(self):
        """
        获取分组页
        """

        return response()

    @request(url='/crm/worklist/changestatus', method='get')
    def changestatus(self):
        """
        改变工单为处理中状态
        """

        _json = {}
        return response(json=_json)

    @request(method='get')
    def worklistgetbyid(self, id):
        """
        查询工单详情
        """

        url = '/crm/worklist/getbyid/{}'.format(id)

        return response(url=url)

    @request(url='/crm/worklist/getdicts', method='get')
    def getdicts(self):
        """
        查询工单字典信息
        """

        _json = {}
        return response(json=_json)

    @request(method='get')
    def getusersbycitydepartment(self, type, id):
        """
        城市部门用户级联查询
        """

        url = '/crm/worklist/getusersbycitydepartment?type={}&id={}'.format(type, id)
            # “city”：全部城市列表[缺省]，“depart”：根据城市ID查询部门，“user”：根据部门ID查询管理员
            # 城市ID或部门ID
            # "isAll":isAll

        return response(url=url)

    @request(url='/crm/worklist/getusersbyname', method='get')
    def getusersbyname(self, name):
        """
        根据名称查询管理员列表
        """

        params = {
            "name": name
        }
        return response(params=params)

    @request(url='/crm/worklist/handle', method='post')
    def workhandle(self, result, wlId):
        """
        处理工单，完成工单
        """

        _json = {
            {
                # "businessId": 0,
                # "businessName": "string",
                # "contactName": "string",
                # "contactPhone": "string",
                # "createdAt": "2018-07-23T01:51:13.676Z",
                # "createdBy": 0,
                # "createdByName": "string",
                # "description": "string",
                # "handledBy": 0,
                # "handledByName": "string",
                # "levelId": 0,
                # "levelName": "string",
                # "orderId": "string",
                "result": result,
                # "sourceId": 0,
                # "sourceName": "string",
                # "status": 0,
                # "typeId": 0,
                # "typeName": "string",
                # "updatedBy": 0,
                "wlId": wlId
            }
        }
        return response(json=_json)

    @request(url='/crm/worklist/handle', method='post')
    def workhandletransfer(self, handledBy, result, wlId):
        """
        处理工单，转接工单
        """

        _json = {
                # "businessId": 0,
                # "businessName": "string",
                # "contactName": "string",
                # "contactPhone": "string",
                # "createdAt": "2018-07-23T01:51:13.676Z",
                # "createdBy": 0,
                # "createdByName": "string",
                # "description": "string",
                "handledBy": handledBy,
                # "handledByName": "string",
                # "levelId": 0,
                # "levelName": "string",
                # "orderId": "string",
                "result": result,
                # "sourceId": 0,
                # "sourceName": "string",
                # "status": 0,
                # "typeId": 0,
                # "typeName": "string",
                # "updatedBy": 0,
                "wlId": wlId
        }
        return response(json=_json)

    @request(url='/crm/worklist/listall', method='post')
    def listall(self):
        """
        查询所有工单列表
        """

        _json = {}
        return response(json=_json)

    @request(url='/crm/worklist/listmy', method='post')
    def listmy(self):
        """
        查询我的工单列表
        """

        _json = {}
        return response(json=_json)

    @request(url='/crm/worklist/save', method='post')
    def worksave(self, contactName, contactPhone, description, handledBy, orderId):
        """
        保存工单
        """

        _json = {
            "businessId": 0,
            # "businessName": "string",
            "contactName": contactName,
            "contactPhone": contactPhone,
            # "createdAt": "2018-07-23T01:51:13.690Z",
            # "createdBy": 0,
            # "createdByName": "string",
            "description": description,
            "handledBy": handledBy,
            # "handledByName": "string",
            "levelId": 0,
            # "levelName": "string",
            "orderId": orderId,
            # "result": "string",
            "sourceId": 0,
            # "sourceName": "string",
            # "status": 0,
            "typeId": 0
            # "typeName": "string",
            # "updatedBy": 0,
            # "wlId": 0
        }
        return response(json=_json)

