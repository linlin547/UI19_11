from Utils.driver import Driver
from Utils.page import Page
import pytest


class TestBNAL:
    def setup_class(self):
        # 关闭更新
        Page.get_home().close_alert()

    def setup(self):
        # 点击我
        Page.get_home().goto_sign()
        # 点击已有账号
        Page.get_sign().goto_login()

    def teardown(self):
        # 点击设置
        Page.get_person().setting_btn()
        # 退出
        Page.get_setting().logout()

    def teardown_class(self):
        # 退出driver
        Driver.quit_app_driver()

    @pytest.mark.parametrize("name, passwd, exp", [("mlili", "159357li", "mlili"),
                                                   (" mlili", "159357li", "mlili"),
                                                   ("13488834010 ", "159357li", "mlili"),
                                                   ("13488834010", "159357li", "mlili")])
    def test_login(self, name, passwd, exp):
        """

        :param name: 账号
        :param passwd: 密码
        :param exp: 预期结果
        :return:
        """
        # 登录操作
        Page.get_login().login(name, passwd)
        # 断言用户名
        assert exp == Page.get_person().get_username()
