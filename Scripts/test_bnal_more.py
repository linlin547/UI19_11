from Utils.driver import Driver
from Utils.page import Page
from Utils.data import Data
import pytest,logging


def value():
    # 列表存储
    data_list = []
    # 读取json
    data = Data.get_json_data("bnal.json")
    # 遍历
    for i in data:
        data_list.append((i.get("account"),
                          i.get("password"),
                          i.get("exp"),
                          i.get("tag"),
                          i.get("desc")))
    return data_list


class TestBNAL:
    def setup_class(self):
        # 关闭更新
        Page.get_home().close_alert()

    def setup(self):
        # 点击我
        Page.get_home().goto_sign()
        # 点击已有账号
        Page.get_sign().goto_login()

    def teardown_class(self):
        # 退出driver
        Driver.quit_app_driver()

    # @pytest.mark.parametrize("name, passwd, exp,tag", [("mlili", "159357li", "mlili", ""),
    #                                                    (" mlili", "159357li", "mlili", ""),
    #                                                    ("13488834010 ", "159357li", "mlili", ""),
    #                                                    ("13488834010", "159357li", "mlili", ""),
    #                                                    ("134888", "159357li", "此用户不存在", "1"),
    #                                                    ("mlili", "159357", "登录密码错误", "1")])
    @pytest.mark.parametrize("name, passwd, exp, tag, desc", value())
    def test_login(self, name, passwd, exp, tag, desc):
        """

        :param name: 账号
        :param passwd: 密码
        :param exp: 预期结果
        :param tag: 有值 代表是预期失败用例
        :param desc: 用例描述信息
        :return:
        """
        logging.info("当前用例:{}".format(desc))
        # 登录操作
        Page.get_login().login(name, passwd)
        # 判断正向用例
        if not tag:
            # 断言用户名
            assert exp == Page.get_person().get_username()
            # 点击设置
            Page.get_person().setting_btn()
            # 退出
            Page.get_setting().logout()
        else:  # 逆向用例
            # 断言 toast消息
            assert Page.get_login().lh.toast_message(exp)

            # 关闭登陆页面
            Page.get_login().close_login()
