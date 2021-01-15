from selenium.webdriver.common.by import By

from Utils.base import BaseObject

import logging


class PersonObject(BaseObject):
    """对象层"""

    def __init__(self):
        super().__init__()
        # 用户名
        self.user_name_id = (By.ID, "com.yunmall.lc:id/tv_user_nikename")
        # 设置按钮
        self.setting_btn_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")

    def find_username(self):
        """定位用户名"""
        return self.search_ele(self.user_name_id)

    def find_setting_btn(self):
        """定位设置按钮"""
        return self.search_ele(self.setting_btn_id)


class PersonHandle:
    """操作层"""

    def __init__(self):
        # 实例化对象层
        self.po = PersonObject()

    def get_user_name(self):
        """获取用户文本"""
        name = self.po.find_username().text
        logging.info("当前获取用户名:{}".format(name))
        return name

    def click_setting_btn(self):
        """点击设置按钮"""
        logging.info("点击设置按钮")
        self.po.find_setting_btn().click()


class PersonTask:
    logging.info("个人中心页面")
    # 实例化操作层
    ph = PersonHandle()

    @classmethod
    def get_username(cls):
        """获取用户名"""
        return cls.ph.get_user_name()

    @classmethod
    def setting_btn(cls):
        """点击设置按钮"""
        cls.ph.click_setting_btn()
