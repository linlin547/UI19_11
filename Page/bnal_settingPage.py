from selenium.webdriver.common.by import By

from Utils.base import BaseObject, BaseHandle
import logging

class SettingObject(BaseObject):
    """对象层"""

    def __init__(self):
        super().__init__()

        # 退出
        self.quit_btn_id = (By.ID, "com.yunmall.lc:id/setting_logout")
        # 确认退出
        self.acc_quit_btn_id = (By.ID, "com.yunmall.lc:id/ymdialog_right_button")

    def find_quit_btn(self):
        """定位退出按钮"""
        # 定位退出
        return self.search_ele(self.quit_btn_id)

    def find_acc_quit_btn(self):
        """定位确认退出按钮"""
        return self.search_ele(self.acc_quit_btn_id)


class SettingHandle(BaseHandle):
    """操作层"""

    def __init__(self):
        # 实例化对象层
        self.so = SettingObject()

    def click_quit_btn(self):
        """点击退出按钮"""

        # 滑动
        self.screen_swipe()
        logging.info("点击退出按钮")
        # 点击
        self.so.find_quit_btn().click()

    def click_acc_quit_btn(self):
        """点击确认退出按钮"""
        logging.info("点击确认退出按钮")
        self.so.find_acc_quit_btn().click()


class SettingTask:
    """业务层"""
    logging.info("设置页面")

    # 实例化操作层
    sh = SettingHandle()

    @classmethod
    def logout(cls):
        """退出"""
        # 点击退出
        cls.sh.click_quit_btn()
        # 点击确认退出
        cls.sh.click_acc_quit_btn()
