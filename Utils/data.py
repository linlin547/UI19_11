import json, os


class Data:

    @classmethod
    def get_json_data(cls, file):
        """
        读取json
        :param file: json文件名字
        :return: json数据
        """
        with open("./Data" + os.sep + file, "r", encoding="utf-8") as f:
            return json.load(f)
