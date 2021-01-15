# class B1:
#     """base对象层"""
#
#     def __init__(self):
#         self.name = "lili"
# 
#     def get_name(self):
#         return self.name
#
#
# class B2:
#     """base对操作"""
#
#     def get_sex(self):
#         return "女"
#
#
# class P1(B1):
#     """页面对象层"""
#
#     def __init__(self):
#         super().__init__()
#
#     def p_name(self):
#         print(self.get_name())
#
#
# #
# class P2(B2, P1):
#     """页面操作层"""
#
#     def __init__(self):
#         # 初始化B2
#         P1.__init__(self)
#
#     def ouput(self):
#         print("p2_self:{}".format(self))
#         # 间接引用B1类方法
#         self.p_name()
#         # 调用B2方法
#         print(self.get_sex())
#
#
# P2().ouput()
