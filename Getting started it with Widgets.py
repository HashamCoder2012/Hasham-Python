from tkinter import *
root=Tk()
root.geometry("400x300")
root.title("Getting started with Widgets")
lbl=Label(text="Enter a number",fg="blue",bg="black")
lbl2=Label(text="Enter another number",fg="orange",bg="yellow")
name_entry=Entry()
name_entry2=Entry()
resultlabel=Label()

def display():
    n1=name_entry.get()
    n2=name_entry2.get()
    prod=n1*n2
    resultlabel.config(text=prod)
btn=Button(text="Calculate",command="Display")
lbl.pack()
name_entry.pack()
lbl2.pack()
name_entry.pack()
btn.pack()
root.mainloop()


