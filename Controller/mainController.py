"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import json
import os

from tkinter import END, messagebox, filedialog
from urllib.request import urlretrieve

from Service.configSet import return_config_path, set_config
from Service.sendRequest import send_request
from View.mainView import Win
from View.adminView import Win as AdminWin
from View.sendInfoView import Win as SendInfoWin
from View.downloadToolsView import Win as DownloadToolsWin
from Controller.downloadToolsController import Controller as DownloadToolsController
from Controller.sendInfoController import Controller as sendInfoController
from Controller.adminController import Controller as AdminController


class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: Win

    def __init__(self):
        self.config_file_path = return_config_path()
        self.config_data = {}

    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        # 启动前执行前置任务
        # 检查文件是否存在
        if os.path.exists(self.config_file_path):
            self.addLog('INFO', '配置文件存在')
            self.addLog('INFO', "config.json 文件存在于:{}".format(self.config_file_path))
        else:
            # 配置文件不存在,弹窗,软件退出
            messagebox.showinfo('error', message="配置文件不存在,软件退出!")
            exit(0)
        # 配置文件存在性检查完毕,现在读取配置文件中的内容,并且设置一些东西
        # TODO 文件读取后赋值,以后只需要读取这个赋值的就可以了
        with open(self.config_file_path, 'r') as f:
            self.config_data = json.load(f)
        print(self.config_data)
        # 设置mac和ip
        set_config(self.config_data)
        self.addLog('INFO', '配置:{}'.format(self.config_data))
        # 将修改后的配置数据写回到文件中
        if self.config_data['first_run'] == 'yes':  # 第一次运行,要求输入班级号,然后日志打印
            self.addLog('WARNING', '第一次运行软件,请汇报班级')
            messagebox.showinfo('WARNING', message="第一次运行软件,请汇报班级")
            # 唤起报告班级号的窗口,向后端报告设备信息由它的按钮事件完成
            sendInfoWin = SendInfoWin(sendInfoController())
            sendInfoWin.mainloop()

    def show_admin(self, evt):
        print("<Double-Button-1>事件未处理:", evt)
        admin_win = AdminWin(AdminController())
        admin_win.mainloop()

    # 检查网络连接
    def check_net_connection(self, evt):
        # 读取名字和当前ip
        msg_level, txt = 'INFO', '网络检查完成,ip:{},该ip没有问题!'.format(self.config_data['address_ip'])
        # ip检查
        if not self.config_data['address_ip'].startswith('192.168') or self.config_data['address_ip'].startswith(
                '10.11'):
            msg_level, txt = 'WARNING', 'ip:{} 不是机器的标准ip'.format(self.config_data['address_ip'])
        # 提示本机ip问题
        self.addLog(msg_level, txt)
        messagebox.showinfo(msg_level, txt)
        self.addLog(msg_level, '发送请求中...')
        try:
            response = send_request(self.config_data['server_url'], 'GET', '/net/netCheck', {})
            request_json = {
                'device_name': self.config_data['device_name'],
                'log_type': 'INFO',
                "log_message": "验证网络正常"
            }
            if response['code'] != 200:  # 机器ip不正常
                request_json['log_type'] = "WARNING"
                request_json['log_message'] = "可以上网,但是可能经过了路由器"

            self.addLog(request_json['log_type'], request_json['log_message'])
            messagebox.showinfo(request_json['log_type'], request_json['log_message'])
            send_request(self.config_data['server_url'], 'POST', '/log/logAdd', request_json)
        except:
            self.addLog('ERROR', '请求发送失败,考虑服务器未启动或机器代理出现问题')
            messagebox.showinfo('ERROR', '请求发送失败,考虑服务器未启动或机器代理出现问题')

    # 报告班级按钮
    def banji_report(self, evt):
        self.addLog('WARNING', '重新汇报班级或报告问题...')
        try:
            # 读取名字和当前ip
            request_json = {
                'device_name': self.config_data['device_name'],
                'log_type': 'WARNING',
                "log_message": "报告了一个问题.或者重新汇报了班级"
            }
            send_request(self.config_data['server_url'], 'POST', '/log/logAdd', request_json)
        except Exception as e:
            self.addLog('ERROR', '请求发送失败,考虑服务器未启动或机器代理出现问题')
            messagebox.showerror("Error", f"网络错误!: {e}")

        sendInfoWin = SendInfoWin(sendInfoController())
        sendInfoWin.mainloop()

    # 下载工具
    def download_tools(self, evt):
        self.addLog('INFO', '下载工具...')
        download_win = DownloadToolsWin(DownloadToolsController())
        download_win.mainloop()

    def addLog(self, msg_level, txt):
        color_map = {
            'INFO': 'green',
            'WARNING': 'orange',
            'ERROR': 'red',
        }
        if msg_level in color_map:
            self.ui.tk_text_log_info.configure(fg=color_map[msg_level])
        # 最后一行插入一行文本
        self.ui.tk_text_log_info.insert(END, "[{}] {}\n".format(msg_level, txt))
        # 翻页到底部
        self.ui.tk_text_log_info.see(END)

    # 软件更新
    def update_shuijing(self, evt):
        print("<Button-1>事件未处理:", evt)
        try:
            # 获取最新版本号并与本机版本号做匹配
            now_version = self.config_data['version_name']
            latest_version = send_request(self.config_data['server_url'], 'GET', '/version/get_latest_Version', {})
            if now_version != latest_version:  # 有最新版本
                # 下载新版本
                messagebox.showerror("INFO", "发现新版本,现在更新!")
                # 文件下载链接
                file_url = "{}/file/download/{}".format(self.config_data['server_url'], latest_version)

                # 弹出文件保存对话框，让用户选择保存路径，并将文件名自动填入
                file_path = filedialog.asksaveasfilename(initialfile=latest_version)
                if not file_path:  # 如果用户取消了保存操作，则返回
                    return
                # 发送HTTP请求并下载文件
                urlretrieve(file_url, file_path)
                messagebox.showinfo("INFO", "新版本下载成功!该版本将自动关闭!请删除该版本")
                self.ui.destroy()

        except Exception as e:
            self.addLog('ERROR', '请求发送失败,考虑服务器未启动或机器代理出现问题')
            messagebox.showerror("Error", f"网络错误!: {e}")
