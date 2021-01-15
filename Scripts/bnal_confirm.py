# from Page.bnal_homePage import HomeTask
# from Page.bnal_signPage import SignTask
# from Page.bnal_loginPage import LoginTask
# from Page.bnal_personPage import PersonTask
# from Page.bnal_settingPage import SettingTask
import time
from Utils.page import Page

"""首页"""
time.sleep(1)
# 关闭更新
# HomeTask.close_alert()
Page.get_home().close_alert()

time.sleep(1)
# 进入我的
# HomeTask.goto_sign()
Page.get_home().goto_sign()

"""注册页"""
# SignTask.goto_login()
Page.get_sign().goto_login()

"""登录页面"""
# LoginTask.login("13488834010", "159357li")
Page.get_login().login("13488834010", "159357li")

"""个人中心页面"""
# 获取用户名
# print(PersonTask.get_username())
print(Page.get_person().get_username())
# 点击设置
# PersonTask.setting_btn()
Page.get_person().setting_btn()

"""设置页面"""
# SettingTask.logout()
Page.get_setting().logout()