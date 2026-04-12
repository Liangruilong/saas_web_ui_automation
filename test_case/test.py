"""
============================
Project: saas_web_ui_automation
Author:Liang RuiLong
Time:2026-03-08 12:05
E-mail:450908351@qq.com
Describe:调试用例
============================
"""
from playwright.sync_api import sync_playwright
import time

# 创建一个playwright上下文管理器
with sync_playwright() as p:
    # 创建一个浏览器（设置为非headless模式）
    browser = p.chromium.launch(headless=False, channel="chrome")
    # 打开一个页面
    page = browser.new_page()
    # 访问saas登登录页
    page.goto("https://pmms01-test.runjian.com/#/login")
    # 等待10秒
    time.sleep(10)
    # 关闭浏览器
    browser.close()
