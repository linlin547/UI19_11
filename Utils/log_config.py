import logging.handlers
import os


def logConfig():
    # 日志器
    logger = logging.getLogger()
    # 设置全局级别
    logger.setLevel(logging.INFO)

    # 控制台处理器
    sh = logging.StreamHandler()

    # 日志位置
    logPath = "./Log" + os.sep + "bnal.log"
    # 文件处理器
    trfh = logging.handlers.TimedRotatingFileHandler(logPath, when="midnight", interval=1,
                                                     backupCount=7, encoding="utf-8")

    # 日志器 添加 控制台处理器
    logger.addHandler(sh)
    # 日志器 添加 文件处理器
    logger.addHandler(trfh)

    # 格式化字符串
    fmt = "%(asctime)s-%(levelname)s-[%(filename)s-%(funcName)s()-%(lineno)d行]-%(message)s"
    # 格式化器
    formatter = logging.Formatter(fmt)

    # 控制台处理器 添加 格式化器
    sh.setFormatter(formatter)
    # 文件处理器 添加 格式化器
    trfh.setFormatter(formatter)
