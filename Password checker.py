from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("400x400")
root.title("Password strenght checker")
lbl=Label("")
def msg():
    MsgBox=messagebox.showinfo("")
    if MsgBox=="ok":
        topwin()