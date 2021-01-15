from Utils.data import Data
import pytest


# 列表套列表
# def value():
#     # 读取数据为 [[],[]]
#     return Data.get_json_data("sum1.json")


# # 列表套字典
# def value():
#     # 数据列表
#     lis = []
#     # 读数据
#     data = Data.get_json_data("sum2.json")
#     # 遍历
#     for i in data:
#         lis.append((i.get("a"), i.get("b"), i.get("c"), i.get("desc")))
#     return lis

# 字典套字典
def value():
    # 数据列表
    lis = []
    # 读数据
    data = Data.get_json_data("sum3.json").get("sum")
    # 遍历
    for i in data:
        lis.append((i.get("a"), i.get("b"), i.get("c"), i.get("desc")))
    return lis


class TestSum:
    # @pytest.mark.parametrize("a, b, c", value())
    @pytest.mark.parametrize("a, b, c,desc", value())
    def test_sum(self, a, b, c, desc):
        """
        加法
        :param a:
        :param b:
        :param c:
        :param desc:用例描述信息
        :return:
        """
        print("\n用例:{}".format(desc))
        print("\n{}+{}=={}".format(a, b, c))
        assert a + b == c
