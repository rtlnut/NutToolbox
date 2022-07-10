from tkinter import *
from tkinter import messagebox

import winreg
import win32api
import win32con
import ctypes, sys

window = Tk()
window.title("NutToolbox")
window.geometry("350x200")
lbl = Label(window, text="ShortCut_icon")
lbl.grid(column=0, row=0)
lbl = Label(window, text="by rtlnut")
lbl.grid(column=0, row=2)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    def delete():
        key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r'Application.Reference')
        winreg.DeleteValue(key, 'IsShortcut')

        print("Delete Complete")
        messagebox.showinfo("Delete Complete", "It takes effect after you restart the computer")


    def add():
        reg_root = win32con.HKEY_CLASSES_ROOT
        reg_path = r'Application.Reference'
        reg_flags = win32con.WRITE_OWNER | win32con.KEY_WOW64_64KEY | win32con.KEY_ALL_ACCESS

        key, _ = win32api.RegCreateKeyEx(reg_root, reg_path, reg_flags)
        # key = win32api.RegOpenKey(reg_root, reg_path, 0, reg_flags)

        win32api.RegSetValueEx(key, "IsShortcut", 0, win32con.REG_SZ, '1')

        win32api.RegCloseKey(key)

        print("Add Complete")
        messagebox.showinfo("Add Complete", "It takes effect after you restart the computer")


    btn = Button(window, text="Delete", command=delete)
    btn.grid(column=1, row=0)
    btn = Button(window, text="Add", command=add)
    btn.grid(column=2, row=0)
    window.mainloop()

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

# I hope no one reads this
# In fact, this project is a piece of s*** :(
