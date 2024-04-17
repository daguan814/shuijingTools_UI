"""
Created on 2024/4/10 22:53 
Author: Shuijing
Description: 
"""
import json
import os
from tkinter import messagebox


from View.mainView import Win as MainWin
from Controller.mainController import Controller as MainUIController

# 将窗口控制器 传递给UI
app = MainWin(MainUIController())

if __name__ == "__main__":
    app.mainloop()
