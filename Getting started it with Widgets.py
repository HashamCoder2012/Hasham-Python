from tkinter import *
root=Tk()
root.geometry("400x300")
root.title("Getting started with Widgets")
lbl=Label(text="Enter a number",fg="blue",bg="black")
lbl2=Label(text="Enter another number",fg="orange",bg="yellow")
name_entry=Entry()
name_entry2=Entry()

def display():
    name=name_entry.get()
    name2=name_entry2.get()
    btn=Button(text="Calculate",command="Display")
    text_box=lbl+lbl2
root.mainloop()


