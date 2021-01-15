from Page.settingPage import SettingTask
from Page.searchPage import SearchTask

# 进入搜索
SettingTask.goto_search_page()

# 打印搜索结果
print("搜索结果:{}".format(SearchTask.search("1")))
