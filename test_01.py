# ！usr/bin/env Python3.11
# -*-coding:utf-8 -*-
from playwright.sync_api import sync_playwright

# input('1....')
# # 启动 playwright driver 进程
# p = sync_playwright().start()
#
# input('2....')
# # 启动浏览器，返回 Browser 类型对象
# browser = p.chromium.launch(headless=False)
# # browser1 = p.firefox.launch()   火狐
# # browser12 = p.webkit.launch()   safri
# # executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome 启动本地浏览器
# # chromium 对应 chromium , edge也对应chromium
# # 创建新页面，返回 Page 类型对象
# page = browser.new_page()
# page.goto("https://www.byhy.net/_files/stock1.html")
# print(page.title()) # 打印网页标题栏
#
# # 输入通讯，点击查询。这是定位与操作，是自动化重点，后文详细讲解
# page.locator('#kw').fill('通讯')  # 输入通讯
# page.locator('#go').click()      # 点击查询
#
# # 打印所有搜索内容
# lcs = page.locator(".result-item").all()
# for lc in lcs:
#     print(lc.inner_text())
#
# input('3....')
# # 关闭浏览器
# browser.close()
# input('4....')
# # 关闭 playwright driver 进程
# p.stop()

# ================
# 方法二：with 省去  p = sync_playwright().start() 和 p.close
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.byhy.net/_files/stock1.html")
    print(page.title())

    page.locator('#kw').fill('通讯')
    page.locator('#go').click()

    lcs = page.locator(".result-item").all()
    for lc in lcs:
        print(lc.inner_text())

    browser.close()