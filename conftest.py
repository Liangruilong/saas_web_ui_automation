"""
============================
Project: saas_web_ui_automation
Author:Liang RuiLong
Time:2026-04-05 21:45
E-mail:450908351@qq.com
Describe:全局配置文件
============================
"""
from pytest import Item
import allure
import pytest
from tools.handle_logs import my_log
from typing import Dict

pytest_plugins = ['plugins.pytest_playwright'] # noqa

def pytest_runtest_call(item: Item):  # noqa
    # 动态添加测试类的 allure.feature()
    if item.parent._obj.__doc__:  # noqa
        allure.dynamic.feature(item.parent._obj.__doc__) # noqa
    # 动态添加测试用例的title 标题 allure.title()
    if item.function.__doc__: # noqa
        allure.dynamic.title(item.function.__doc__) # noqa

@pytest.fixture(autouse=True)
def set_log_case_name(request):
    """
    自动获取函数注释定义的用例标题，注入到日志中和allure.title 完全保持一致
    """
    # 1. 获取和allure一模一样的用例标题
    case_title = request.node.function.__doc__ if request.node.function.__doc__ else request.node.name

    # 2. 给日志注入用例标题
    def filter_record(record):
        record.case_name = case_title.strip()
        return True

    my_log.addFilter(filter_record)
    # 用例开始日志
    my_log.info(f"{'=' * 60} 开始执行：{case_title} {'=' * 60}")

    yield  # 执行测试用例

    # 用例结束日志
    my_log.info(f"{'=' * 60} 执行完成：{case_title} {'=' * 60}\n")
    my_log.filters.remove(filter_record)
