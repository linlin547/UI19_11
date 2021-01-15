import pytest

from Utils.driver import Driver
from Page.settingPage import SettingTask
from Page.searchPage import SearchTask


class TestSearch:

    def setup_class(self):
        # 点击搜索按钮
        SettingTask.goto_search_page()

    def teardown_class(self):
        """退出driver"""
        Driver.quit_app_driver()

    @pytest.mark.parametrize("search_text, search_result", [("1", "休眠"), ("i", "IP地址"), ("m", "MAC地址")])
    def test_search(self, search_text, search_result):
        """
        测试方法
        :param search_text: 搜索内容
        :param search_result: 预期结果
        :return:
        """
        # 输入搜索内容
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys(search_text)

        # self.bh.input_text(self.bo.search_ele(self.search_input), search_text)
        # 获取搜索结果
        # res = self.driver.find_elements_by_id("com.android.settings:id/title")
        # res = self.bo.search_eles(self.search_result)
        # 断言
        assert search_result in SearchTask.search(search_text)
