"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import json
from tkinter import END, filedialog, messagebox
from urllib.request import urlretrieve

from Service.configSet import return_config_path
from Service.sendRequest import send_request
from View.downloadToolsView import Win


# 示例下载 https://www.pytk.net/blog/1702564569.html
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
        # TODO 组件初始化 赋值操作
        # 获取全部文件信息
        # 读取配置文件,获取server_url
        try:
            with open(self.config_file_path, 'r') as f:
                self.config_data = json.load(f)
            response_data = send_request(self.config_data['server_url'], 'GET', '/file/getAllFilesInfo', '')
            data = response_data['data']
            print(data)
            # TODO 创建表格时,将数据插入表中
            for item in data:
                self.ui.tk_table_file.insert('', END, values=(
                    item['file_id'],
                    item['file_name'],
                    item['upload_time'][:10],
                    item['download_time'][:10],
                    item['download_count'],
                    item['file_type'],
                    item['file_size']
                ))
        except Exception as e:
            messagebox.showerror("Error", f"网络错误!: {e}")

    def download_file(self, evt):
        # print("<Double-Button-1>事件未处理:", evt)
        # 获取被双击的行的标识符
        item_id = self.ui.tk_table_file.identify_row(evt.y)
        # 获取被双击行的所有数据
        row_value = self.ui.tk_table_file.item(item_id, 'values')
        # 提取filename字段的值
        file_name = row_value[1]
        print(file_name)

        # 发送下载请求
        try:
            # 文件下载链接
            file_url = "{}/file/download/{}".format(self.config_data['server_url'], file_name)

            # 弹出文件保存对话框，让用户选择保存路径，并将文件名自动填入
            file_path = filedialog.asksaveasfilename(initialfile=file_name)
            if not file_path:  # 如果用户取消了保存操作，则返回
                return

            def report_progress(block_num, block_size, total_size):
                downloaded = block_num * block_size
                progress = min(int(downloaded / total_size * 100), 100)
                self.ui.tk_progressbar_jindu['value'] = progress

            # 发送HTTP请求并下载文件
            urlretrieve(file_url, file_path, reporthook=report_progress)

            messagebox.showinfo("Download", "文件下载成功!")
        except Exception as e:
            messagebox.showerror("Error", f"下载失败: {e}")
