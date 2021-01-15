from Page.bnal_homePage import HomeTask
from Page.bnal_signPage import SignTask
from Page.bnal_loginPage import LoginTask
from Page.bnal_personPage import PersonTask
from Page.bnal_settingPage import SettingTask


class Page:
    """返回所有页面类"""

    @classmethod
    def get_home(cls):
        """返回首页类"""
        return HomeTask

    @classmethod
    def get_sign(cls):
        """返回注册页面类"""
        return SignTask

    @classmethod
    def get_login(cls):
        """返回登录页面"""
        return LoginTask

    @classmethod
    def get_person(cls):
        """返回个人中心"""
        return PersonTask

    @classmethod
    def get_setting(cls):
        """返回设置页面"""
        return SettingTask
