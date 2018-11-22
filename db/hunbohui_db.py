from common.utils import DB
from utils.cfg import CONFIG

# 定义hunbbohui数据库
hunbbohui_db = DB(CONFIG.HUNBOHUI_DATABASE)


def get_content_from_phone(l):
    """
    通过电话号码查询数据库获取短信信息
    """
    return hunbbohui_db.query("select sms_content from c_sms_log where phone ="+str(l) +" order by sms_id desc limit 1")[0]['sms_content']


# def get_label_name_by_target_id(_id):
#     """
#     从target id查询label name
#     """
#     res = bops_db.query('select label_name from tbd_label_binding where is_deleted=0 and target_id=%s' % _id)
#     return [i.label_name for i in res]


if __name__ == '__main__':
    pass