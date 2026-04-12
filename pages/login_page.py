"""
============================
Project: saas_web_ui_automation
Author:Liang RuiLong
Time:2026-03-08 17:34
E-mail:450908351@qq.com
Describe:登录页面
============================
"""
from playwright.sync_api import Page

import time

import allure

from playwright.sync_api import sync_playwright

from config.login_info import login_info

from tools.handle_logs import my_log


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('#form_item_account')
        self.password_input = page.locator('#form_item_password')
        self.login_button = page.locator('//span[text() ="登 录"]')
        # 用户输入框，密码输入框提示语
        self.username_tip = page.locator('//div[text()= "手机号/邮箱/用户名"]')
        self.password_tip = page.locator('//div[text()= "请输入密码"]')

    def navigate(self):
        with allure.step("导航到注册页"):
            my_log.info("导航到注册页: /register.html")
            self.page.goto("/#/login")

    def fill_username(self, username):
        with allure.step(f"输入用户名:{username}"):
            my_log.info(f"输入用户名:{username}")
            self.username_input.fill(username)

    def fill_password(self, password):
        with allure.step("输入登录密码"):
            my_log.info("输入登录密码")
            self.password_input.fill(password)

    def click_login_button(self):
        with allure.step("点击登录按钮"):
            my_log.info("点击登录按钮")
            self.login_button.click()

    def login(self, username, password) -> None:
        """完整的登录流程"""
        self.fill_username(username)
        self.fill_password(password)
        self.login_button.click()

if __name__ == '__main__':
    with sync_playwright() as p:
        # 创建一个浏览器（设置为非headless模式）
        browser = p.chromium.launch(headless=False,channel="chrome")
        # 打开一个页面
        page = browser.new_page()
        # 访问saas登登录页
        page.goto("https://pmms01-test.runjian.com/#/login")
        # 等待10秒
        time.sleep(5)
        login = LoginPage(page)
        login.login(login_info['user_name'], login_info['password'])
        # 关闭浏览器
        browser.close()