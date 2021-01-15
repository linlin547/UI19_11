from selenium.webdriver.common.by import By

from Utils.base import BaseObject
import logging

class HomeObject(BaseObject):
    """首页对象类"""

    def __init__(self):
        super().__init__()
        # 弹窗关闭按钮
        self.alert_btn = (By.ID, "com.yunmall.lc:id/img_close")
        # 我
        self.my_btn = (By.ID, "com.yunmall.lc:id/tab_me")

    def find_alert_btn(self):
        """定位弹窗关闭按钮"""
        return self.search_ele(self.alert_btn)

    def find_my_btn(self):
        """首页我的按钮"""
        return self.search_ele(self.my_btn)


class HomeHandle:
    """首页操作类"""

    def __init__(self):
        # 实例化首页对象类
        self.ho = HomeObject()

    def click_alert_btn(self):
        """点击弹窗关闭按钮"""
        logging.info("关闭更新弹窗")
        self.ho.find_alert_btn().click()

    def click_my_btn(self):
        """点击首页我的按钮"""
        logging.info("点击我")
        self.ho.find_my_btn().click()


class HomeTask:
    """首页业务类"""
    logging.info("首页")

    # 实例化首页操作类
    hh = HomeHandle()

    @classmethod
    def close_alert(cls):
        """关闭更新弹窗"""
        cls.hh.click_alert_btn()

    @classmethod
    def goto_sign(cls):
        """点击首页我的"""
        cls.hh.click_my_btn()
