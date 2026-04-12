"""
============================
Project: saas_web_ui_automation
Author:Liang RuiLong
Time:2026-04-10 16:25
E-mail:450908351@qq.com
Describe:路径处理
============================
"""
import os
import time

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)

# 错误截图路径
error_image_dir = os.path.join(base_dir, "error_images")
print(error_image_dir)

# 上传图片的路径
image_dir = os.path.join(base_dir, r"resources\test.jpg")
print(image_dir)

# 日志路径
log_file_name = time.strftime("%Y%m%d", time.localtime())
log_dir = os.path.join(base_dir, "logs", f"{log_file_name}.log")
print(log_dir)