from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("400x400")
root.title("Password strenght checker")
btn=Button(root,text="your password is weak",color="Green")

label1=Label(root,text="Hey user!,Welcome to Password strenght checker app")
def msg():
    MsgBox=messagebox.showinfo("Alert","is you password lenght from 6 to 8")
    if MsgBox=="ok":
        print("The password is weak")
    else:
        print("The password is strong")
root.mainloop()