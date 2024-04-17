"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import json
from tkinter import messagebox
from Service.configSet import return_config_path
from Service.sendRequest import send_request
from View.sendInfoView import Win


# 示例下载 https://www.pytk.net/blog/1702564569.html
class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: Win

    def __init__(self):
        pass

    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        # TODO 组件初始化 赋值操作

    # 向后端报告设备信息
    def sendDeviceInfo(self, evt):
        config_file_path = return_config_path()
        with open(config_file_path, 'r') as f:
            config_data = json.load(f)
        print(config_data)
        base_url = config_data['server_url']
        nianji = self.ui.tk_select_box_nianji.get()
        banji = self.ui.tk_select_box_banji.get()
        config_data['device_name'] = '{}年{}班'.format(nianji, banji)
        another_info = self.ui.tk_input_buchong.get()
        json_data = {
            "device_name": config_data['device_name'],  # 从输入框读取
            "another_info": another_info,  # 从输入框读取
            "address_mac": config_data['address_mac'],
            "address_ip": config_data['address_ip']
        }
        try:
            response = send_request(base_url, 'POST', '/device/report', json_data)
            print(response)

            # 弹窗表示上传成功

            messagebox.showinfo('INFO', message=response['msg'])
            # 关闭窗口
            config_data['first_run'] = 'no'
            # 将修改后的配置数据写回到文件中
            with open(config_file_path, 'w') as f:
                json.dump(config_data, f)
            self.ui.destroy()
            print("上报班级完成", evt)
        except:
            messagebox.showinfo('ERROR', message="上传失败,服务器未启动!")
            # 在日志中写入这个错误!
