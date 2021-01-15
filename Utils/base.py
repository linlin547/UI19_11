from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from Utils.driver import Driver
import time,logging


class BaseObject:

    def __init__(self):
        self.driver = Driver.get_app_driver()

    def search_ele(self, loc, timeout=5, poll=1.0):
        """
        定位单个元素
        :param loc: 元组 (定位类型,属性值) (By.ID,"ccc")...
        :param timeout: 搜索元素超时时间
        :param poll: 搜索间隔
        :return: 定位对象
        """
        logging.info("操作元素:{}".format(loc))
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(loc[0], loc[1]))

    def search_eles(self, loc, timeout=5, poll=1.0):
        """
        定位一组元素
        :param loc: 元组 (定位类型,属性值) (By.ID,"ccc")...
        :param timeout: 搜索元素超时时间
        :param poll: 搜索间隔
        :return: 定位对象列表
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(loc[0], loc[1]))


class BaseHandle:
    """操作类"""

    def input_text(self, ele, text):
        """
        输入文本
        :param ele: 输入框对象
        :param text: 输入内容
        :return:
        """
        logging.info("输入内容:{}".format(text))
        # 清空
        ele.clear()
        # 输入
        ele.send_keys(text)

    def screen_swipe(self, tag=1):
        """
        滑动方法
        :param tag: 1：↑ 2: ↓ 3: ← 4: →
        :return:
        """
        driver = Driver.get_app_driver()
        # 分辨率
        size = driver.get_window_size()
        # 宽
        width = size.get("width")
        # 高
        height = size.get("height")

        # 等待
        time.sleep(1.5)

        if tag == 1:
            logging.info("向上滑动")
            # 宽*50%,高*80% -> 宽*50%,高*20%
            driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, 1500)
        if tag == 2:
            logging.info("向下滑动")
            # 宽*50%,高*20% -> 宽*50%,高*80%
            driver.swipe(width * 0.5, height * 0.2, width * 0.5, height * 0.8, 1500)
        if tag == 3:
            logging.info("向左滑动")
            # 宽*80%,高*50% -> 宽*20%,高*50%
            driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5, 1500)
        if tag == 4:
            logging.info("向右滑动")
            # 宽*20%,高*50% -> 宽*80%,高*50%
            driver.swipe(width * 0.2, height * 0.5, width * 0.8, height * 0.5, 1500)

    def toast_message(self, mess, tag="a"):
        """
        定位toast消息
        :param mess: toast完整内容
        :param tag: a:app w:web
        :return: 定位到返回True 定位不到返回False
        """
        if tag == "a":
            mess = (By.XPATH, "//*[contains(@text,'{}')]".format(mess))
        if tag == "w":
            mess = (By.XPATH, "//*[contains(text(),'{}')]".format(mess))
        try:
            # 定位toast
            BaseObject().search_ele(mess, 3, 0.3)
            logging.info("toast文本:{} 存在".format(mess))
            return True
        except TimeoutException:
            logging.info("toast文本:{} 不存在".format(mess))
            # 定位不到元素
            return False
