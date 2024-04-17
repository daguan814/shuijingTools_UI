"""
Created on 2024/4/11 15:46 
Author: Shuijing
Description: 
"""
import netifaces


# 获取本机IP
def get_local_ip():
    try:
        # 获取本机所有网络接口的信息
        interfaces = netifaces.interfaces()

        # 遍历每个网络接口
        for interface in interfaces:
            # 获取网络接口的地址族为AF_INET（IPv4）的IP地址信息
            if netifaces.AF_INET in netifaces.ifaddresses(interface):
                # 获取网络接口的IP地址信息
                ip_addresses = netifaces.ifaddresses(interface)[netifaces.AF_INET]

                # 遍历每个IP地址信息
                for ip_address in ip_addresses:
                    # 获取IP地址
                    local_ip = ip_address['addr']

                    # 排除回环地址（127.0.0.1）
                    if not local_ip.startswith('127'):
                        return local_ip
    except Exception as e:
        print("获取本机 IP 地址失败:", e)
        return '0.0.0.0'

# 获取本机MAC
def get_local_mac_address():
    try:
        # 获取本机所有网络接口的信息
        interfaces = netifaces.interfaces()

        # 遍历每个网络接口
        for interface in interfaces:
            # 获取网络接口的地址族为AF_LINK（MAC地址）的信息
            if netifaces.AF_LINK in netifaces.ifaddresses(interface):
                # 获取网络接口的MAC地址信息
                mac_addresses = netifaces.ifaddresses(interface)[netifaces.AF_LINK]

                # 遍历每个MAC地址信息
                for mac_address in mac_addresses:
                    # 获取MAC地址
                    local_mac_address = mac_address['addr']
                    return local_mac_address
    except Exception as e:
        print("获取本机 MAC 地址失败:", e)
        return "aa:aa:aa:aa:aa:aa:aa"
