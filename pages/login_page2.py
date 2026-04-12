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

from playwright.sync_api import sync_playwright

from config.login_info import login_info


class LoginPage:
    user_name_input = {'loc': '//input[@id = "form_item_account"]', 'page_action': '登录页面用户名输入框'}
    password_input = {'loc': '//input[@id = "form_item_password"]', 'page_action': '登录页面密码输入框'}
    login_button = {'loc': '//span[text() ="登 录"]', 'page_action': '登录页面验证码输入框'}

    def __init__(self):
        pass  # pass 表示空实现

    # 成功登录行为
    # def login_success(self):
    #     # 输入用户名
    #     self.base_page.element_input(locations=self.user_name_input['loc'], page_action=self.user_name_input['page_action'], value=login_info['user_name'])
    #     # 输入密码
    #     self.base_page.element_input(locations=self.password_input['loc'], page_action=self.password_input['page_action'], value=login_info['password'])
    #     # 点击登录按钮
    #     self.base_page.element_click(locations=self.login_button['loc'], page_action=self.login_button['page_action'])


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
        login = LoginPage()
        page.locator(login.user_name_input['loc']).fill(login_info['user_name'])
        page.locator(login.password_input['loc']).fill(login_info['password'])
        page.locator(login.login_button['loc']).click()
        time.sleep(10)
        # 关闭浏览器
        browser.close()