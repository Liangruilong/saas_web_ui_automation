"""
============================
Project: webdriver_test
Author:Sanrui
Time:2025-06-12 22:33
E-mail:13826493156@qq.com
Describe:SAAS测试环境登录测试用例
============================
"""
import pytest
from pages.login_page import LoginPage
from playwright.sync_api import expect


class TestLogin:
    """登录功能"""

    @pytest.fixture(autouse=True)  # autouse=True 的作用是：当前类（或模块）下的所有测试用例，会自动执行这个 fixture
    def for_each(self, page):
        self.login = LoginPage(page)
        self.login.navigate()  # 进入登录页面
        yield
        print("后置操作")

    def test_login_success(self):
        """登录成功"""
        self.login.fill_username('cxp4')
        self.login.fill_password('cxp@123456')
        self.login.click_login_button()
        # 等待页面跳转到目标URL（自动等待，超时默认30秒）
        self.login.page.wait_for_url(url="**#/station-overview/index", wait_until="networkidle")
        expect(self.login.page).to_have_title("电站总览 - 智慧电站平台")
        expect(self.login.page).to_have_url("#/station-overview/index")


    def test_login_fail1(self):
        """用户名为空，点击登录"""
        self.login.fill_username('')
        self.login.fill_password('123456')
        self.login.click_login_button()
        # 断言
        expect(self.login.username_tip).to_be_visible()
        expect(self.login.username_tip).to_contain_text("手机号/邮箱/用户名")

    def test_login_fail2(self):
        """密码为空，点击登录"""
        self.login.fill_username('cxp4')
        self.login.fill_password('')
        self.login.click_login_button()
        # 断言
        expect(self.login.username_tip).to_be_visible()
        expect(self.login.username_tip).to_contain_text("手机号/邮箱/用户名")

    def test_login_fail3(self):
        """密码为空，点击登录"""
        self.login.fill_username('cxp4')
        self.login.fill_password('')
        self.login.click_login_button()
        # 断言
        expect(self.login.username_tip).to_be_visible()
        expect(self.login.username_tip).to_contain_text("手机号/邮箱/用户名")