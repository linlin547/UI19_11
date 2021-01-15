from selenium.webdriver.common.by import By

from Utils.base import BaseObject

#
# class SettingObject:
#     """对象层"""
#
#     def __init__(self):
#         # 实例化BaseObject
#         self.bo = BaseObject()
#         """页面元素"""
#         # 搜索按钮
#         self.search_btn = (By.ID, "com.android.settings:id/search")
#
#     def find_search_btn(self):
#         """返回搜索按钮定位对象"""
#         return self.bo.search_ele(self.search_btn)


class SettingObject(BaseObject):
    # 继承父类 减少重复实例化和对象调用
    """对象层"""

    def __init__(self):
        super().__init__()
        """页面元素"""
        # 搜索按钮
        self.search_btn = (By.ID, "com.android.settings:id/search")

    def find_search_btn(self):
        """返回搜索按钮定位对象"""
        return self.search_ele(self.search_btn)

class SettingHandle:
    """操作层"""

    def __init__(self):
        # 实例化对象层
        self.so = SettingObject()

    def click_setting_btn(self):
        """点击搜索按钮"""
        self.so.find_search_btn().click()


class SettingTask:
    """业务层"""

    # 实例化操作层
    sh = SettingHandle()

    @classmethod
    def goto_search_page(cls):
        """进入搜索页面"""
        cls.sh.click_setting_btn()
