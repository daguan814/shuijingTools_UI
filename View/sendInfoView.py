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


class WinGUI(Toplevel):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_select_box_nianji = self.__tk_select_box_nianji(self)
        self.tk_select_box_banji = self.__tk_select_box_banji(self)
        self.tk_input_buchong = self.__tk_input_buchong(self)
        self.tk_label_luuoioqg = self.__tk_label_luuoioqg(self)
        self.tk_button_luuomtt8 = self.__tk_button_luuomtt8(self)

    def __win(self):
        self.title("发送设备信息")
        # 设置窗口大小、居中
        width = 400
        height = 180
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

    def __tk_select_box_nianji(self, parent):
        cb = Combobox(parent, state="readonly", bootstyle="default")
        cb['values'] = ("年级", "7", "8", "9")
        cb.place(relx=0.0725, rely=0.0833, relwidth=0.3750, relheight=0.1667)
        return cb

    def __tk_select_box_banji(self, parent):
        cb = Combobox(parent, state="readonly", bootstyle="default")
        cb['values'] = (
        "班级", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
        "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30")
        cb.place(relx=0.5750, rely=0.0833, relwidth=0.3750, relheight=0.1667)
        return cb

    def __tk_input_buchong(self, parent):
        ipt = Entry(parent, bootstyle="default")
        ipt.place(relx=0.0625, rely=0.4167, relwidth=0.8875, relheight=0.3167)
        return ipt

    def __tk_label_luuoioqg(self, parent):
        label = Label(parent, text="维护信息:", anchor="center", bootstyle="default")
        label.place(relx=0.0625, rely=0.2778, relwidth=0.1500, relheight=0.1111)
        return label

    def __tk_button_luuomtt8(self, parent):
        btn = Button(parent, text="发送", takefocus=False, bootstyle="default")
        btn.place(relx=0.4475, rely=0.7778, relwidth=0.1250, relheight=0.1667)
        return btn


class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)

    def __event_bind(self):
        self.tk_button_luuomtt8.bind('<Button>', self.ctl.sendDeviceInfo)
        pass

    def __style_config(self):
        sty = Style()
        sty.configure(self.new_style(self.tk_label_luuoioqg), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_button_luuomtt8), font=("微软雅黑", -12))
        pass


if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()