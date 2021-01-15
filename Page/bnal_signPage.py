from selenium.webdriver.common.by import By

from Utils.base import BaseObject
import logging

class SignObject(BaseObject):
    """注册对象层"""

    def __init__(self):
        super().__init__()

        # 已有账号去登陆
        self.exits_account_id = (By.ID, "com.yunmall.lc:id/textView1")

    def find_exit_account(self):
        """定位已有账号"""
        return self.search_ele(self.exits_account_id)


class SignHandle:
    """操作层"""

    def __init__(self):
        # 实例化对象层
        self.so = SignObject()

    def click_exits_account(self):
        """点击已有账号去登陆"""
        logging.info("点击已有账号去登陆")
        self.so.find_exit_account().click()


class SignTask:
    logging.info("注册页面")

    # 实例化操作层
    sh = SignHandle()

    @classmethod
    def goto_login(cls):
        """进入登录页面"""
        cls.sh.click_exits_account()
