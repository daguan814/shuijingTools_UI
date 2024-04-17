"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import random
from tkinter import *
from tkinter.ttk import *
from ttkbootstrap import *
from pytkUI.widgets import *


class WinGUI(Window):
    def __init__(self):
        super().__init__(themename="cosmo", hdpi=False)
        self.__win()
        self.tk_label_log_label = self.__tk_label_log_label(self)
        self.tk_label_frame_net = self.__tk_label_frame_net(self)
        self.tk_button_check_net_button = self.__tk_button_check_net_button(self.tk_label_frame_net)
        self.tk_label_lutw2obj = self.__tk_label_lutw2obj(self)
        self.tk_label_luukmizs = self.__tk_label_luukmizs(self)
        self.tk_text_log_info = self.__tk_text_log_info(self)
        self.tk_label_frame_lv0spnig = self.__tk_label_frame_lv0spnig(self)
        self.tk_button_banji_report_button = self.__tk_button_banji_report_button(self.tk_label_frame_lv0spnig)
        self.tk_button_lv38lll9 = self.__tk_button_lv38lll9(self.tk_label_frame_lv0spnig)
        self.tk_label_frame_lv0vc2bb = self.__tk_label_frame_lv0vc2bb(self)
        self.tk_button_download_tools_button = self.__tk_button_download_tools_button(self.tk_label_frame_lv0vc2bb)

    def __win(self):
        self.title("水镜运维助手")
        # 设置窗口大小、居中
        width = 600
        height = 400
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)

        self.minsize(width=width, height=height)

    def scrollbar_autohide(self, vbar, hbar, widget):
        """自动隐藏滚动条"""

        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)

        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)

        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())

    def v_scrollbar(self, vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')

    def h_scrollbar(self, hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')

    def create_bar(self, master, widget, is_vbar, is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)

    def new_style(self, widget):
        ctl = widget.cget('style')
        ctl = "".join(random.sample('0123456789', 5)) + "." + ctl
        widget.configure(style=ctl)
        return ctl

    def __tk_label_log_label(self, parent):
        label = Label(parent, text="系统日志", anchor="center", bootstyle="default")
        label.place(relx=0.5000, rely=0.0000, relwidth=0.5000, relheight=0.0525)
        return label

    def __tk_label_frame_net(self, parent):
        frame = LabelFrame(parent, text="基础运维", bootstyle="default")
        frame.place(relx=0.0117, rely=0.2700, relwidth=0.4667, relheight=0.3425)
        return frame

    def __tk_button_check_net_button(self, parent):
        btn = Button(parent, text="检查网络", takefocus=False, bootstyle="default")
        btn.place(relx=0.0179, rely=0.0000, relwidth=0.4286, relheight=0.2555)
        return btn

    def __tk_label_lutw2obj(self, parent):
        label = Label(parent, text="版本:V1.0 开放使用时间:7:30-22:30", anchor="center", bootstyle="default")
        label.place(relx=0.0000, rely=0.8750, relwidth=1.0000, relheight=0.0500)
        return label

    def __tk_label_luukmizs(self, parent):
        label = Label(parent, text="开发:云梦实中 水镜", anchor="center", bootstyle="default")
        label.place(relx=0.0000, rely=0.9250, relwidth=1.0000, relheight=0.0750)
        return label

    def __tk_text_log_info(self, parent):
        text = Text(parent)
        text.place(relx=0.4983, rely=0.0625, relwidth=0.4883, relheight=0.8075)
        self.create_bar(parent, text, True, False, 299, 25, 293, 323, 600, 400)
        return text

    def __tk_label_frame_lv0spnig(self, parent):
        frame = LabelFrame(parent, text="软件维护", bootstyle="default")
        frame.place(relx=0.0083, rely=0.0475, relwidth=0.4700, relheight=0.1900)
        return frame

    def __tk_button_banji_report_button(self, parent):
        btn = Button(parent, text="班级报告", takefocus=False, bootstyle="default")
        btn.place(relx=0.0177, rely=0.0000, relwidth=0.4433, relheight=0.4605)
        return btn

    def __tk_button_lv38lll9(self, parent):
        btn = Button(parent, text="软件更新", takefocus=False, bootstyle="default")
        btn.place(relx=0.5319, rely=0.0132, relwidth=0.4078, relheight=0.4605)
        return btn

    def __tk_label_frame_lv0vc2bb(self, parent):
        frame = LabelFrame(parent, text="辅助工具", bootstyle="default")
        frame.place(relx=0.0117, rely=0.6400, relwidth=0.4667, relheight=0.2125)
        return frame

    def __tk_button_download_tools_button(self, parent):
        btn = Button(parent, text="工具下载", takefocus=False, bootstyle="default")
        btn.place(relx=0.0357, rely=0.0000, relwidth=0.4107, relheight=0.4118)
        return btn


class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)

    def __event_bind(self):
        self.tk_label_log_label.bind('<Double-Button-1>', self.ctl.show_admin)
        self.tk_button_check_net_button.bind('<Button-1>', self.ctl.check_net_connection)
        self.tk_button_banji_report_button.bind('<Button-1>', self.ctl.banji_report)
        self.tk_button_lv38lll9.bind('<Button-1>', self.ctl.update_shuijing)
        self.tk_button_download_tools_button.bind('<Button-1>', self.ctl.download_tools)
        pass

    def __style_config(self):
        sty = Style()
        sty.configure(self.new_style(self.tk_label_log_label), font=("微软雅黑", -13))
        sty.configure(self.new_style(self.tk_button_check_net_button), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_label_lutw2obj), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_label_luukmizs), font=("微软雅黑", -14, "bold italic"))
        sty.configure(self.new_style(self.tk_button_banji_report_button), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_button_lv38lll9), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_button_download_tools_button), font=("微软雅黑", -12))
        pass


if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()