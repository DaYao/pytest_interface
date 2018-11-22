# @Time    :2018/11/19 9:51
# @Author  :lvjunjie
from apis.free_ticket_online_api import FreeTicket
from data.online.free_ticket_online_data import FreeTicketOnlineCase
import pytest

free_ticket_online_case_data = FreeTicketOnlineCase().free_ticket_index_online()
free_ticket_inputphone_online_case_data = FreeTicketOnlineCase().free_ticket_inputphone()


class TestFreeTicket:

    @pytest.mark.parametrize('data', free_ticket_online_case_data)
    def test_索票首页(self, data):
        free_ticket = FreeTicket()
        res = free_ticket.free_ticket_index(data['city'])
        # print(res.text)
        assert res.status_code == 200, "接口响应" + str(res.status_code)
        assert res.elapsed.seconds <=5, "接口响应超时"
        for i in data["assert_data"]:
            assert i in res.text, "接口响应异常"

    @pytest.mark.parametrize('data', free_ticket_online_case_data)
    def test_索票expo页面(self, data):
        free_ticket = FreeTicket()
        res = free_ticket.free_ticket_expo_index(data['city'])
        # print(res.text)
        assert res.status_code == 200, "接口响应" + str(res.status_code)
        assert res.elapsed.seconds <= 5, "接口响应超时"
        print(data["assert_data"])
        for i in data["assert_data"]:
            assert i in res.text, "接口响应异常"

    @pytest.mark.parametrize('data', free_ticket_inputphone_online_case_data)
    def test_索票接口(self, data):
        free_ticket = FreeTicket()
        res = free_ticket.free_ticket_save_inputphone(city=data['city'])
        print(res.json['err'])
        assert res.status_code == 200, "接口响应" + str(res.status_code)
        assert res.elapsed.seconds <= 5, "接口响应超时"
        assert res.json['err'] == "hapn.ok", "接口响应异常"

