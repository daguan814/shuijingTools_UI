"""
Created on 2024/4/11 09:59
Author: Shuijing
Description:
"""
import os

from Service.getLocalInfo import get_local_ip, get_local_mac_address


# 获取配置项的地址
def return_config_path():
    # 获取项目的根目录
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_file_path = os.path.join(project_root, "config", "config.json")
    return config_file_path


# 读取配置设置
def set_config(config_data):
    # 读取配置信息,将ip和mac都写到配置里面
    config_data['address_ip'] = get_local_ip()
    config_data['address_mac'] = get_local_mac_address()
    print(config_data)
    return config_data
