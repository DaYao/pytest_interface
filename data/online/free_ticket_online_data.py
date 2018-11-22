# @Time    :2018/11/19 9:50
# @Author  :lvjunjie

datano_to_city = {
    "[data0]": "杭州",
    "[data1]": "北京",
    "[data2]": "武汉",
    "[data3]": "上海",
    "[data4]": "广州",
    "[data5]": "天津",
}

class FreeTicketOnlineCase:
    def free_ticket_index_online(self):
        return [
            {
                "city": "hz",
                "assert_data": ["杭州婚博会官网", "中国婚博会官网", "杭州婚博会免费索票"]
            },
            {
                "city": "bj",
                "assert_data": ["北京婚博会官网", "中国婚博会官网", "北京婚博会免费索票"]
            },
            {
                "city": "wh",
                "assert_data": ["武汉婚博会官网", "中国婚博会官网", "武汉婚博会免费索票"]
            },
            {
                "city": "sh",
                "assert_data": ["上海婚博会官网", "中国婚博会官网", "上海婚博会免费索票"]
            },
            {
                "city": "gz",
                "assert_data": ["广州婚博会官网", "中国婚博会官网", "广州婚博会免费索票"]
            },
            {
                "city": "tj",
                "assert_data": ["天津婚博会官网", "中国婚博会官网", "天津婚博会免费索票"]
            },
        ]

    def free_ticket_inputphone(self):
        return [
            {
                "city": "hz",
                "phone": "15157163734",
                "spouse_phone": "18958033079"
            },
            {
                "city": "bj",
                "phone": "15157163734",
                "spouse_phone": "18958033079"
            },
            {
                "city": "wh",
                "phone": "15157163734",
                "spouse_phone": "18958033079"
            },
            {
                "city": "sh",
                "phone": "15157163734",
                "spouse_phone": "18958033079"
            },

            {
                "city": "gz",
                "phone": "15157163734",
                "spouse_phone": "18958033079"
            },
            {
                "city": "tj",
                "phone": "15157163734",
                "spouse_phone": "18958033079"
            }
        ]

