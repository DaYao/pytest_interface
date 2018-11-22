# @Time    :2018/10/29 16:57
# @Author  :lvjunjie
from datetime import datetime
from py.xml import html
import pytest
import os
from common.result_processing import ResultProcessing,Alarm
from data.online.free_ticket_online_data import datano_to_city

nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
alarm_list = ['test_free_ticket.py', 'test_suites/test_online/test_free_ticket.py']
result_processing = ResultProcessing()
alarm = Alarm()
product_id = 1
to_login_names = os.getenv('to_login_names', '')


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    cells.insert(3, html.th('Time', class_='sortable time', col='time'))
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(html.pre(report.description)))
    cells.insert(3, html.td(datetime.utcnow(), class_='col-time'))
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    try:
        description = item.function.__doc__.decode('utf-8')
    except:
        description = item.function.__doc__
    # description = html.br.join(description.split('\n'))

    report.description = description

# def pytest_exception_interact(node, call, report):
#     # print('--------------------pytest_exception_interact--------------------------------')
#     print(node)
#     print(call)
#     print(report.location)
#     tc_name = str(report.location[0]).replace('\\t','\\\\t')
#     failed_content = str(call)
#     print('tc_name=============================' + tc_name)
#     print(tc_name + '' + str(node) + '失败，失败原因：' + failed_content)
#     # failed_content = str(call)
#     # result_processing.result_processing('failed', tc_name, tc_name + '' + str(node) + '失败，失败原因：' + failed_content)
#     # alarm.service_alarm_email(tc_name + '' + str(node) + '失败，失败原因：' + failed_content)


def pytest_runtest_logreport(report):
    # print('--------------- pytest_runtest_logreport ---------------------')
    print(report.when)
    print(report.location)
    print(report.outcome)
    try:
        test_result = report.outcome
        # tc_name = str(report.location[0]).replace('\\t','\\\\t')
        # # print('tc_name=============================' + tc_name)
        if test_result == 'failed' and report.location[0] in alarm_list:
            city = datano_to_city[report.location[2][-7:]]
            content = report.location[2][:-7] + "   " + city + \
                      "失败啦！！！！请进入http://172.16.200.100:8080/jenkins/job/%E7%B4%A2%E7%A5%A8%E4%B8%9A%E5%8A%A1%E7%9B%91%E6%8E%A7/allure/  查看结果" \
                      + nowTime
            print(content)
            # print(to_login_names)
            # print(to_login_names.split(","))
            print("接口异常，准备发发送钉钉消息至" + to_login_names)
            # alarm.service_alarm_dingding(content, to_login_names.split(","))
    except:
        pass