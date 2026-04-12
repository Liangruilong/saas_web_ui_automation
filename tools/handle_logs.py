"""
============================
Project: saas_web_ui_automation
Author:Liang RuiLong
Time:2026-04-10 16:27
E-mail:450908351@qq.com
Describe:日志收集
============================
"""
# import logging
#
# from tools.handle_path import log_dir
#
# from logging import handlers
#
# def my_log():

    # # 1、创建日志收集器
    # # 左侧的py52是一个Python变量，用于存储logging.getLogger()返回的日志收集器（Logger）对象。
    # # 右侧的py52是 getLogger()方法的参数，用于 唯一标识日志收集器的名称。日志系统内部通过这个 name 管理不同的 Logger 实例。相同 name 的多次调用会返回同一个 Logger 对象（避免重复创建）。
    # py52 = logging.getLogger(name="py52")
    #
    # # 2、创建日志输出渠道
    # pycharm = logging.StreamHandler()  # 1.log,2.log
    # # 文件渠道
    # log_file = handlers.TimedRotatingFileHandler(filename=log_dir, interval=1, when="D", backupCount=20,
    #                                              encoding="utf-8")
    # # 3、日志格式
    # ft = ">>>%(asctime)s-%(name)s-%(levelname)s-%(filename)s: %(message)s "
    # log_style = logging.Formatter(fmt=ft)
    #
    # # 4、日志格式绑定(渠道)
    # pycharm.setFormatter(fmt=log_style)
    # log_file.setFormatter(fmt=log_style)
    #
    # # 5、设置日志级别(收集器的日志级别(大)debug，输出渠道的日志级别(小)info)
    # # 一般情况下只设置收集器的日志级别，渠道会继承收集器的日志级别
    # # pycharm.setLevel(logging.INFO) #无需设置
    # py52.setLevel(logging.DEBUG)
    #
    # # 6、将日志输出渠道绑定到日志收集器上
    # py52.addHandler(pycharm)
    # py52.addHandler(log_file)
    #
    # # 7、关闭日志传播（避免日志重复输出）
    # py52.propagate = False
    # return py52
import logging
from tools.handle_path import log_dir
from logging import handlers

# 自定义过滤器：支持用例标题
class CaseFilter(logging.Filter):
    def filter(self, record):
        record.case_name = getattr(record, 'case_name', '全局日志')
        return True


def my_log():
    py52 = logging.getLogger(name="py52")
    # 关键：清空旧处理器，解决日志重复打印问题
    py52.handlers.clear()

    # 输出渠道
    pycharm = logging.StreamHandler()
    log_file = handlers.TimedRotatingFileHandler(filename=log_dir, interval=1, when="D", backupCount=20,
                                                 encoding="utf-8")

    # 日志格式：新增 [用例标题]
    ft = ">>>%(asctime)s-[%(case_name)s]-%(name)s-%(levelname)s-%(filename)s: %(message)s "
    log_style = logging.Formatter(fmt=ft)

    # 绑定格式
    pycharm.setFormatter(log_style)
    log_file.setFormatter(log_style)

    # 绑定过滤器
    py52.addFilter(CaseFilter())

    # 日志级别
    py52.setLevel(logging.DEBUG)

    # 添加渠道
    py52.addHandler(pycharm)
    py52.addHandler(log_file)

    # 关闭传播
    py52.propagate = False
    return py52


# 单例模式
my_log = my_log()
