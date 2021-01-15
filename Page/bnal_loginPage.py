from selenium.webdriver.common.by import By

from Utils.base import BaseObject, BaseHandle
import logging

class LoginObject(BaseObject):
    """对象层"""

    def __init__(self):
        super().__init__()
        # 元素 -账号
        self.account_id = (By.ID, "com.yunmall.lc:id/logon_account_textview")
        # 元素 -密码
        self.passwd_id = (By.ID, "com.yunmall.lc:id/logon_password_textview")
        # 元素 -登录按钮
        self.login_btn_id = (By.ID, "com.yunmall.lc:id/logon_button")
        # 元素 - 关闭登陆按钮
        self.close_login_btn = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")

    def find_account(self):
        """定位账号"""
        return self.search_ele(self.account_id)

    def find_password(self):
        """定位密码"""
        return self.search_ele(self.passwd_id)

    def find_login_btn(self):
        """定位点击按钮"""
        return self.search_ele(self.login_btn_id)

    def find_close_login_btn(self):
        """定位关闭页面按钮"""
        return self.search_ele(self.close_login_btn)


# 没有继承页面对象层---写法
# class LoginHandle(BaseHandle):
#     """操作层"""
#
#     def __init__(self):
#         # 实例化对象层
#         self.lo = LoginObject()
#
#     def input_account(self, name):
#         """
#         输入账号
#         :param name: 账号
#         :return:
#         """
#         self.input_text(self.lo.find_account(), name)
#
#     def input_password(self, pwd):
#         """
#         输入密码
#         :param pwd: 密码
#         :return:
#         """
#         self.input_text(self.lo.find_password(), pwd)
#
#     def click_login_btn(self):
#         """点击登录按钮"""
#         self.lo.find_login_btn().click()

# 继承页面对象层----写法
class LoginHandle(BaseHandle, LoginObject):
    """操作层"""

    def __init__(self):
        # 初始化对象层的init方法
        LoginObject.__init__(self)

    def input_account(self, name):
        """
        输入账号
        :param name: 账号
        :return:
        """
        logging.info("输入账号")
        self.input_text(self.find_account(), name)

    def input_password(self, pwd):
        """
        输入密码
        :param pwd: 密码
        :return:
        """
        logging.info("输入密码")
        self.input_text(self.find_password(), pwd)

    def click_login_btn(self):
        """点击登录按钮"""
        logging.info("点击登录按钮")
        self.find_login_btn().click()

    def click_close_login_btn(self):
        """关闭登录页面"""
        logging.info("关闭登陆页面")
        self.find_close_login_btn().click()


class LoginTask:
    logging.info("登录页面")

    # 实例化操作层
    lh = LoginHandle()

    @classmethod
    def login(cls, name, pwd):
        """
        登录
        :param name: 用户名
        :param pwd: 密码
        :return:
        """
        # 输入用户
        cls.lh.input_account(name)
        # 输入密码
        cls.lh.input_password(pwd)
        # 点击登录
        cls.lh.click_login_btn()

    @classmethod
    def close_login(cls):
        cls.lh.click_close_login_btn()
